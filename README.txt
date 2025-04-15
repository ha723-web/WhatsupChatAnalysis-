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
- ☁️ **Word Cloud**: Visualize common words
- ⏰ **Hourly Activity**: Messages sent by hour of the day
- 📅 **Weekly Activity**: Messages sent by day of the week
- 📈 **Interactive Plots**: Built with Matplotlib and WordCloud

---

## 🔧 Project Structure (YAML Format)

```yaml
whatsup-analyzer:
  app.py: "Main Streamlit application"
  helper.py: "Helper functions (optional)"
  preprocessor.py: "Preprocessing logic (optional)"
  README.md: "Project documentation"
  requirements.txt: "Python pip dependencies"
  environment.yml: "Conda environment setup"
  sample_data:
    example_chat.txt: "Sample WhatsApp chat export"

---

## Commands to run 
