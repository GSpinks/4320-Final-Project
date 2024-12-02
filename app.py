from flask import Flask, render_template, request, flash, url_for
from markupsafe import Markup
import csv
import os
from time import time
import sqlite3

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "your secret key"

def get_cost_matrix():
    cost_matrix = [[100, 75, 50, 100] for row in range(12)]
    return cost_matrix

def db_connect():
    conn = sqlite3.connect('reservations.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations")
    res_rows = cursor.fetchall()
    cursor.execute("SELECT * FROM admins")
    admin_rows = cursor.fetchall()
    return res_rows, admin_rows

@app.route('/', methods=['GET', 'POST'])
def index():




    return render_template('index.html')

