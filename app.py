from flask import Flask, request, session, flash, redirect, render_template, url_for
from dotenv import load_dotenv
import psycopg2.extras
import psycopg2
import hashlib
import sqlite3
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Set secret key from environment variable
app.secret_key = os.getenv("FLASK_SECRET_KEY", "default-secret-key")

# 
def get_connection():
    # Connect to PostgreSQL (Adjust connection parameters as needed) relevant 
    conn = psycopg2.connect(
        # On Render:
        dbname="library_class_version_m4n7", # Database
        user="library_class_version_m4n7_user", #Username
        password="Cm5Yp036HJQVGdiDA0x9sq3iyAvPBRnO",# Password
        # External Database URL:
        # postgresql://library_class_version_m4n7_user:Cm5Yp036HJQVGdiDA0x9sq3iyAvPBRnO@dpg-csgtodggph6c73bseubg-a.frankfurt-postgres.render.com/library_class_version_m4n7
        host="dpg-csgtodggph6c73bseubg-a.frankfurt-postgres.render.com",  # Or the hostname of your PostgreSQL server
        port="5432",  # Default port for PostgreSQL
    )
    return conn

# List of all books from the DB
def get_books():
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute("SELECT * FROM Books")
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return books

# Display of all books 
@app.route("/")
def book_list():
    books = get_books()
    return render_template("books.html", books=books)


# Get user by username
def get_user_by_username(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE Name = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user

# Authenticate user
def authenticate(username, password):
    user = get_user_by_username(username)
    if user:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return user["Password"] == hashed_password
    return False

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if authenticate(username, password):
            session["username"] = username
            return redirect(url_for("book_list"))
        else:
            flash("Invalid credentials. Please try again.")
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)