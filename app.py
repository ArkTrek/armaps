import csv
import os
from datetime import datetime
from flask import Flask, render_template, request
from user_agents import parse

app = Flask(__name__)
CSV_FILE = "logs.csv"

# Ensure CSV file exists with headers
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Serial No", "Date", "Time", "Browser", "Browser Version", "OS", "OS Version", 
                         "Device", "Brand", "Model", "Is Mobile", "Is Tablet", "Is Touch", "Is PC", "Is Bot", "User-Agent"])

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    parsed_ua = parse(user_agent)

    # Get current date and time
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    # Get device details
    device_info = [
        date,
        time,
        parsed_ua.browser.family,  # Browser Name
        parsed_ua.browser.version_string,  # Browser Version
        parsed_ua.os.family,  # OS Name
        parsed_ua.os.version_string,  # OS Version
        parsed_ua.device.family,  # Device Name
        parsed_ua.device.brand or "Unknown",  # Device Brand
        parsed_ua.device.model or "Unknown",  # Device Model
        parsed_ua.is_mobile,  # Is Mobile?
        parsed_ua.is_tablet,  # Is Tablet?
        parsed_ua.is_touch_capable,  # Is Touchscreen?
        parsed_ua.is_pc,  # Is PC?
        parsed_ua.is_bot,  # Is Bot?
        user_agent  # Full User-Agent String
    ]

    # Get last serial number and increment
    with open(CSV_FILE, "r") as file:
        lines = list(csv.reader(file))
        serial_no = int(lines[-1][0]) + 1 if len(lines) > 1 else 1  # Start from 1

    # Append new entry
    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([serial_no] + device_info)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
