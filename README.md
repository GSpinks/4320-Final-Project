# 4320 Final Project: Bus Reservation System

This is a simple Flask-based bus reservation system designed for IT students attending a ski trip/hackathon in Colorado. The system allows students to reserve seats on the bus and provides an admin portal to view the seating chart and total sales.

## Features
- **Admin Login**: Admin can log in to view the seating chart and total sales.
- **Reservations**: Passengers can view an interactive seating chart and make reservations for available seats.
- **Seating Chart**: Displays reserved and available seats using a color-coded chart.

## Requirements

- Python 3.x
- Flask 2.2.5

## Setup Instructions

1. Clone the repository.
   ```bash
   git clone https://github.com/GSpinks/4320-Final-Project
   ```
2. Change your directory to that of the project
   ```bash
   cd 4320-Final-Project
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the application:
   ```bash
   python app.py
   ```

The app will be available at `http://localhost:5000`.

## Docker Setup (Optional)

To run the application inside a Docker container:

1. Build the Docker image:
   ```bash
   docker-compose build
   ```
2. Start the container:
   ```bash
   docker-compose up
   ```

## Database

The database `reservations.db` is used to store reservation data. The schema is defined in `schema.sql`.
