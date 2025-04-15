# 📱 WhatsApp Chat Analyzer

A Streamlit-powered web app to analyze your WhatsApp chat exports in `.txt` or `.zip` format. Visualize chat trends, user activity, word clouds, and emoji stats—all in a few clicks!

---

## 🚀 Features

- 📁 **File Support**: Upload `.txt` or `.zip` WhatsApp chat exports  
- 📊 **Chat Stats**:
  - Total messages
  - Most active user
  - Top 5 most common words
  - Emoji usage summary (total + top 5)
- ☁️ **Word Cloud**: Visualize most used words
- ⏰ **Hourly Activity**: Message counts by hour of the day
- 📅 **Weekly Activity**: Message activity by day of the week
- 📈 **Interactive Visuals**: Built with `Matplotlib` & `WordCloud`

---

## 🛠️ Tech Stack

| Category            | Technology             |
|---------------------|------------------------|
| **Language**        | Python 3.x             |
| **Framework**       | Streamlit              |
| **Data Handling**   | Pandas                 |
| **Visualization**   | Matplotlib, WordCloud  |
| **Emoji Analysis**  | emoji (Python library) |
| **Deployment**      | Local via Streamlit    |

---

## 📁 Project Structure

```yaml
whatsup-analyzer/
├── app.py              # Main Streamlit application
├── helper.py           # Helper functions (optional)
├── preprocessor.py     # Preprocessing logic (optional)
├── requirements.txt    # Python pip dependencies
├── environment.yml     # (Optional) Conda environment setup
├── README.md           # Project documentation
└── sample_data/
    └── example_chat.txt   # Sample WhatsApp chat file

---

## 📁 Commands to Run

```yaml

python3 -m venv venv
source venv/bin/activate
pip install streamlit pandas matplotlib wordcloud emoji
streamlit run app.py

---