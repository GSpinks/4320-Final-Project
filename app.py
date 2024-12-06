from flask import Flask, render_template, request, redirect, url_for
from markupsafe import Markup
import csv
import os
from time import time
import sqlite3

from flask import Flask, render_template, request, redirect, url_for, flash

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
    return render_template('Admin.html')

@app.route('/reservations', methods=['GET', 'POST'])
def reservations():
    return render_template('Reservations.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0")

