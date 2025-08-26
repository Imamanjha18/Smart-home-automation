# Smart Home Automation System

A comprehensive Flask-based web application for controlling IoT devices through a web interface with real-time updates, automation scheduling, and user authentication.

## Features

- **Device Control**: Control smart home devices via MQTT

- **Real-time Updates**: WebSocket support for live device status updates

- **Automation Scheduling**: Create time-based or trigger-based automation rules

- **User Authentication**: Secure user login and registration system

- **Responsive Dashboard**: Mobile-friendly web interface

- **REST API**: JSON API for integration with other systems

- **Notification System**: Get alerts for device status changes

## Technologies Used

- **Backend**: Python, Flask, Flask-SocketIO, Flask-Login, Flask-SQLAlchemy

- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap, jQuery

- **Database**: SQLite (can be configured for PostgreSQL/MySQL)

- **Communication**: MQTT (Paho MQTT Client)

- **Scheduling**: APScheduler for automation tasks

- **Real-time**: Socket.IO for live updates

## Installation

1. Clone the repository:
git clone (https://github.com/Imamanjha18/Smart-home-automation)

2. cd smart-home-automation

3. Create and activate a virtual environment:
python -m venv venv

source venv/bin/activate (On Linux/Mac)

venv\Scripts\Activate.ps1 (On Windows (PowerShell))

venv\Scripts\activate (On Windows (cmd))

4. Install dependencies:
pip install -r requirements.txt

## Run

Start the Flask application:
flask run

The app will be available at:
👉 http://localhost:5000

## Screenshots
<img width="1824" height="871" alt="Screenshot (32)" src="https://github.com/user-attachments/assets/f8202cdd-09a2-4f70-82e9-1b2eed378971" />
