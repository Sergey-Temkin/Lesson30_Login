from flask import Flask, request, session, flash, redirect, render_template, url_for
from dotenv import load_dotenv
import hashlib
import sqlite3
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Set secret key from environment variable
app.secret_key = os.getenv("FLASK_SECRET_KEY", "default-secret-key")

# List of all books from the DB
def get_books():
    conn = sqlite3.connect("library.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Books")
    books = cursor.fetchall()
    conn.close()
    return books

# Display of all books 
@app.route("/")
def book_list():
    books = get_books()
    return render_template("books.html", books=books)


# Get user by username
def get_user_by_username(username):
    conn = sqlite3.connect("library.db")
    conn.row_factory = sqlite3.Row
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