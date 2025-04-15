import streamlit as st
import re
from collections import Counter
from datetime import datetime
import emoji
import io
import zipfile
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd

st.set_page_config(page_title="📊 WhatsApp Chat Analyzer", layout="wide")

st.title("📱 WhatsApp Chat Analyzer")
st.markdown("Upload a WhatsApp `.txt` file or `.zip` from your export to explore chat insights and visuals.")

uploaded_file = st.file_uploader("Upload WhatsApp `.txt` or `.zip` file", type=["txt", "zip"])

# === Load and Parse ===
def extract_chat_file(uploaded):
    if uploaded.name.endswith(".zip"):
        with zipfile.ZipFile(uploaded) as z:
            for name in z.namelist():
                if name.endswith(".txt"):
                    return z.read(name).decode("utf-8")
    else:
        return uploaded.read().decode("utf-8")
    return None

def parse_chat(chat_text):
    lines = chat_text.split("\n")
    messages, users, dates = [], [], []
    current_msg, current_user, current_date = "", "", None

    pattern = re.compile(r'^\[(\d{1,2}/\d{1,2}/\d{2,4}),\s(\d{1,2}:\d{2}:\d{2})\u202f(AM|PM)\]\s(.+?):\s(.*)')

    for line in lines:
        match = pattern.match(line)
        if match:
            if current_msg:
                messages.append(current_msg.strip())
                users.append(current_user)
                dates.append(current_date)

            datetime_str = f"{match.group(1)} {match.group(2)} {match.group(3)}"
            try:
                current_date = datetime.strptime(datetime_str, "%m/%d/%y %I:%M:%S %p")
            except:
                try:
                    current_date = datetime.strptime(datetime_str, "%m/%d/%Y %I:%M:%S %p")
                except:
                    current_date = None

            current_user = match.group(4)
            current_msg = match.group(5)
        else:
            current_msg += " " + line.strip()

    if current_msg:
        messages.append(current_msg.strip())
        users.append(current_user)
        dates.append(current_date)

    return users, messages, dates

# === Analysis ===
def show_analysis(users, messages, dates):
    st.subheader("📊 Basic Chat Stats")

    st.write(f"**Total Messages:** {len(messages)}")
    user_counts = Counter(users)
    top_user, top_count = user_counts.most_common(1)[0]
    st.write(f"**Most Active User:** {top_user} ({top_count} messages)")

    word_counter = Counter()
    all_emojis = []

    for msg in messages:
        words = re.findall(r'\b\w+\b', msg.lower())
        word_counter.update(words)
        all_emojis += [ch for ch in msg if ch in emoji.EMOJI_DATA]

    st.write("**Top 5 Common Words:**")
    for word, count in word_counter.most_common(5):
        st.write(f"- {word}: {count}")

    emoji_counter = Counter(all_emojis)
    st.write(f"**Total Emojis Used:** {len(all_emojis)}")
    if emoji_counter:
        st.write("**Top 5 Emojis:**")
        for emo, count in emoji_counter.most_common(5):
            st.write(f"- {emo}: {count}")

    # === Word Cloud ===
    st.subheader("☁️ Word Cloud")
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(word_counter)
    fig_wc, ax_wc = plt.subplots()
    ax_wc.imshow(wordcloud, interpolation="bilinear")
    ax_wc.axis("off")
    st.pyplot(fig_wc)

    # === Hourly Activity ===
    st.subheader("⏰ Hourly Activity")
    df = pd.DataFrame({"user": users, "message": messages, "datetime": dates})
    df["hour"] = df["datetime"].dt.hour

    fig_hr, ax_hr = plt.subplots()
    df["hour"].value_counts().sort_index().plot(kind="bar", ax=ax_hr)
    ax_hr.set_xlabel("Hour of Day")
    ax_hr.set_ylabel("Message Count")
    st.pyplot(fig_hr)

    # === Weekly Activity ===
    st.subheader("📅 Weekly Activity")
    df["weekday"] = df["datetime"].dt.day_name()
    fig_wd, ax_wd = plt.subplots()
    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    df["weekday"].value_counts().reindex(weekday_order).plot(kind="bar", ax=ax_wd)
    ax_wd.set_xlabel("Day of Week")
    ax_wd.set_ylabel("Message Count")
    st.pyplot(fig_wd)

      # === Hourly Activity ===
    st.subheader("⏰ Hourly Activity")

    # User input to filter hours
    max_hour = st.slider("Select the end hour for activity visualization (24-hour format)", min_value=0, max_value=23, value=23)

    df = pd.DataFrame({"user": users, "message": messages, "datetime": dates})
    df["hour"] = df["datetime"].dt.hour

    # Filter by user-selected hour
    filtered_df = df[df["hour"] <= max_hour]

    fig_hr, ax_hr = plt.subplots()
    filtered_df["hour"].value_counts().sort_index().plot(kind="bar", ax=ax_hr)
    ax_hr.set_xlabel("Hour of Day")
    ax_hr.set_ylabel("Message Count")
    st.pyplot(fig_hr)



# === Main Flow ===
if uploaded_file:
    chat_text = extract_chat_file(uploaded_file)
    if chat_text:
        users, messages, dates = parse_chat(chat_text)
        show_analysis(users, messages, dates)
    else:
        st.error("❌ Could not read a valid .txt chat file from the ZIP.")
