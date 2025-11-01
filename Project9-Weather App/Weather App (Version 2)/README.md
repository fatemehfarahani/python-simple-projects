# Weather App (Version 2) - Flask Web Application

A modern weather web application built with **Python (Flask)** as the backend.  
This app allows users to check the current weather for any city using the [OpenWeatherMap API](https://openweathermap.org/api).

---

## Features

- User-friendly web interface for checking weather
- Get current temperature, weather description, humidity, and wind speed for any city
- Error handling for invalid city names
- **Backend (server-side) code is fully written by me in Python/Flask**
- **Frontend and CSS styles are inspired by and adapted from [this GeeksforGeeks project](https://www.geeksforgeeks.org/software-engineering/forecast-weather-project-check-today-weather-for-any-location/)**

---

## How It Works

- The user enters a city name in the web form.
- The Flask backend sends a request to the OpenWeatherMap API and retrieves the weather data.
- The weather information is displayed on the web page with a modern and attractive design.

---
## Requirements

- Python 3.10
- [Flask](https://pypi.org/project/Flask/)
- [requests](https://pypi.org/project/requests/)

## How to Use

1. **Clone the repository or copy the code into a folder.**
2. **Get a free API key from [OpenWeatherMap](https://openweathermap.org/api) and set it in the `API_KEY` variable in the code.**
3. **Install the required dependencies:**
    ```bash
    pip install flask requests
    ```
4. **Make sure you have the following files and folders:**
    - `weather_app.py` (the main Flask app)
    - `templates/index.html` (the HTML template)
    - `static/style.css` (the CSS file)
    - Any images used for background or icons in `static/images/` (if needed)

5. **Run the Flask app:**
    ```bash
    weather_app.py
    ```
6. **Open your browser and go to:**  
    [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

7. **Enter a city name and see the weather information!**


