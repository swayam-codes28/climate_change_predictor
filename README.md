# 🌧️ Weather & Flood Alert System

A Python-based application that provides **real-time weather updates**, **rain alerts**, and **flood warnings** using live data from `wttr.in`.

This project is designed to help users—especially farmers and general users—make informed decisions based on rainfall and weather conditions.

---

## 🚀 Features

- 🌍 Predefined list of **high-rain and flood-prone cities**
- 🔍 Supports **custom city input**
- 🌤 Fetches **live weather data**
- 🌧 Detects rain using:
  - Weather description
  - Precipitation levels (mm)
- 🚨 Generates **flood warnings** based on:
  - Heavy rainfall
  - Hourly precipitation trends
- 📊 Simple and user-friendly **console output**

---

## 🧠 How It Works

1. User selects a city (number or name)
2. The system fetches weather data from `wttr.in`
3. It analyzes:
   - Current weather condition
   - Rainfall (mm)
   - Hourly precipitation
4. Displays:
   - ✅ Safe irrigation message  
   - ⚠️ Rain alert  
   - 🚨 Flood warning  

---

## 🛠️ Tech Stack

- Python 🐍
- Requests Library
- wttr.in API

---

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/weather-flood-alert.git
cd weather-flood-alert
Install dependencies:
pip install requests
▶️ Usage

Run the program:

python weather_alert.py

Then:

Enter a city number
OR type a city name
OR press Enter for default (Cherrapunji)
📌 Example Output
📍 Location: Mumbai
🌤 Current Weather: Light rain
🌧 Rainfall (mm): 3.2

⚠️ RAIN ALERT!
🌧 Rain expected soon. Farmers should avoid irrigation.

🚨 FLOOD WARNING!
⚡ Heavy rainfall / storm detected.
🌊 Flood risk possible in low-lying areas.
🎯 Use Cases
🌾 Smart farming decisions
🌊 Flood risk awareness
📚 Learning API integration in Python
🧪 Beginner-friendly project
🔮 Future Improvements
GUI (Tkinter / Web Interface)
SMS / Email alerts
Machine Learning predictions
Historical weather analysis
👨‍💻 Author

Swayam Prakash Tripathi
