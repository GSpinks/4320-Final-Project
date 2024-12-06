from flask import Flask, render_template, request, redirect, url_for
from markupsafe import Markup
import csv
import os
from time import time
import sqlite3

from flask import Flask, render_template, request, redirect, url_for, flash


def db_connect():
    return sqlite3.connect('reservations.db')

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "your_secret_key"

@app.route('/', methods=['GET', 'POST'])
def index():
    error_message = None  # Default is no error
    if request.method == 'POST':
        selected_option = request.form.get('page')
        if selected_option == "choose":
            error_message = "Please select a valid option from the dropdown."
        elif selected_option == 'admin':
            return redirect(url_for('admin'))
        elif selected_option == 'reservations':
            return redirect(url_for('reservations'))
    return render_template('index.html', error_message=error_message)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    error_message = None
    show_chart = False
    seating_chart = None
    total_sales = 0  # Default: no sales

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Connect to the database
        conn = db_connect()
        cursor = conn.cursor()
        # Query the admins table
        cursor.execute("SELECT * FROM admins WHERE username = ? AND password = ?", (username, password))
        admin = cursor.fetchone()

        if admin:
            show_chart = True
            seating_chart = generate_seating_chart()
            total_sales = calculate_total_sales(seating_chart)
        else:
            error_message = "Invalid username or password. Please try again."

        conn.close()

    return render_template('Admin.html', error_message=error_message, show_chart=show_chart, seating_chart=seating_chart, total_sales=total_sales)

def generate_seating_chart():
    # Define the seating chart dimensions
    rows = 12  # Number of rows
    columns = 4  # Number of columns
    seating_chart = [['O' for _ in range(columns)] for _ in range(rows)]

    # Connect to the database
    conn = db_connect()
    cursor = conn.cursor()
    # Get all reserved seats
    cursor.execute("SELECT seatRow, seatColumn FROM reservations")
    reserved_seats = cursor.fetchall()
    conn.close()

    # Mark reserved seats as 'X'
    for seat in reserved_seats:
        row, col = seat
        # Ensure row and column indices are within bounds
        if 0 <= row < rows and 0 <= col < columns:
            seating_chart[row][col] = 'X'  # No adjustment needed if database is 0-indexed
        else:
            print(f"Warning: Invalid seat coordinates ({row}, {col}) ignored.")

    return seating_chart


def get_cost_matrix():
    """Generates a 12 x 4 cost matrix"""
    cost_matrix = [[100, 75, 50, 100] for _ in range(12)]
    return cost_matrix

def calculate_total_sales(seating_chart):
    """Calculates the total sales based on reserved seats and the cost matrix"""
    cost_matrix = get_cost_matrix()
    total_sales = 0

    for row_index, row in enumerate(seating_chart):
        for col_index, seat in enumerate(row):
            if seat == 'X':  # Reserved seat
                total_sales += cost_matrix[row_index][col_index]

    return total_sales


@app.route('/reservations', methods=['GET'])
def reservations():
    # Generate the seating chart
    seating_chart = generate_seating_chart()
    return render_template('Reservations.html', seating_chart=seating_chart)


if __name__ == '__main__':
    app.run(host="0.0.0.0")

