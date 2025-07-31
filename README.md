# 🌦️ Weather Forecast App

A modern, responsive Flask-based Weather App using the WeatherAPI.  
It shows current weather, 5-day forecast, and supports automatic location detection, dark/light mode, and weather-based background visuals.

---

## 🔗 Live Demo

👉 [Click here to view the live app](https://weather-app-by-adarsh.up.railway.app)

![App Preview](assets/preview.png) <!-- Replace with actual image path -->

---

## 🚀 Features

✅ Get **current weather** details  
✅ View **5-day forecast**  
✅ **Auto-detect location** using your browser  
✅ **Responsive** across mobile, tablet, and desktop  
✅ Toggle between **Light & Dark Mode**  
✅ Dynamic background based on **weather condition**  
✅ Search **history log** stored in session  

---

## 🧑‍💻 Tech Stack

- Python & Flask
- HTML, CSS, JavaScript
- WeatherAPI (https://weatherapi.com)
- Bootstrap for styling

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/weather-app.git
cd weather-app

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🔑 Setup

1. Get a free API key from [https://www.weatherapi.com](https://www.weatherapi.com)
2. Replace the key in `app.py`:

```python
API_KEY = 'your_actual_api_key_here'
```

---

## ▶️ Run Locally

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## ☁️ Deployment on Railway

Make sure these files exist:

- `requirements.txt`
- `Procfile` → with content:
  ```txt
  web: python app.py
  ```
- In `app.py`, replace:

```python
app.run(debug=True)
```

With:

```python
import os
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)
```

---

## 📂 Project Structure

```
weather-app/
│
├── app.py
├── requirements.txt
├── Procfile
├── README.md
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   └── js/
```

---

## 📌 Future Improvements

- Add weather-based animations (e.g., snow falling, clouds moving)
- Store history in a database
- Add hourly forecast
- Add voice assistant for weather

---

## 📝 License

This project is open-source and free to use under the [MIT License](LICENSE).

---

## 💬 Feedback

Got a suggestion or bug report? Feel free to open an issue or contact me.

---

### ❤️ Created with love by Adarsh
