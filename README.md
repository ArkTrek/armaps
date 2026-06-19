# Ar Maps: Interactive Map & Device Logger 🌍

![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey.svg)
![Leaflet](https://img.shields.io/badge/Leaflet-Interactive%20Maps-green.svg)

> **Disclaimer:** This project is for demonstration purposes only and is not the final product. It serves as a foundational prototype that can be modified and scaled into a very neat and unique codebase as needed.

## 📖 Overview

**Ar Maps** is a lightweight web application that seamlessly integrates an interactive mapping interface with automated background user-agent logging. Built using Python and Flask, the application serves a dynamic Leaflet map centered on Kerala, India, while silently capturing detailed client-side telemetry (browser, OS, device model, touch capabilities) into a structured CSV file. 

## ✨ Features

- **Interactive Mapping:** Utilizes `Leaflet.js` for smooth, responsive map rendering.
- **Custom Location Import:** Includes a dynamic "G" button that parses Google Maps URLs, extracts the coordinates, and drops custom markers directly onto the Leaflet map.
- **Background Telemetry Logging:** Automatically detects and logs visitor data upon page load, saving details to a continuously updated `logs.csv`. Logged data includes:
  - Date & Time
  - Browser (Name & Version)
  - Operating System (Name & Version)
  - Device specific (Brand, Model, Mobile/Tablet/PC/Touch-capable)
  - Bot detection
- **Dynamic UI Elements:** Features auto-hiding headers and footers to maximize map visibility, alongside smooth CSS transitions.

## 🛠️ Tech Stack

- **Backend:** Python 3.10, Flask
- **Data Handling:** `csv`, `user_agents`
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Mapping Library:** Leaflet.js

## 🚀 Getting Started

### Prerequisites

Ensure you have **Python 3.10** installed on your system. 

### Installation

1. **Clone the repository:**
```bash
   git clone [https://github.com/arktrek/armaps.git](https://github.com/arktrek/armaps.git)
   cd ar-maps

```


2. **Create a virtual environment (optional but recommended):**
```bash
python3.10 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

```


3. **Install the required dependencies:**
```bash
pip install -r requirements.txt

```



### Running the Application

1. Start the Flask server:
```bash
python app.py

```


2. Open your web browser and navigate to:
```text
[http://127.0.0.1:5000](http://127.0.0.1:5000)

```



## 📂 Project Structure

```text
├── app.py               # Main Flask application and CSV logging logic
├── logs.csv             # Auto-generated telemetry data (created on first run)
├── static/
│   ├── script.js        # Core map logic, UI toggles, and URL parsing
│   ├── styles.css       # Layout, map container, and dynamic UI styling
│   └── faviconn.ico     # Site favicon
└── templates/
    └── index.html       # Main HTML template containing Leaflet integration

```

## 💡 How It Works

1. **The Request:** When a user visits the root URL (`/`), Flask intercepts the request and grabs the `User-Agent` string.
2. **The Processing:** The `user_agents` library parses this string to determine exactly what device and software the visitor is using.
3. **The Logging:** A new sequential entry is appended to `logs.csv` with the timestamped device data.
4. **The Interface:** Flask renders `index.html`, displaying the full-screen map interface where users can interact with existing markers or add new ones via Google Maps links.

## 👤 Author

**Arpit Ramesan** (ArkTrek)

* Contact: arpitramesan777@gmail.com
