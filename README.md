# Lesson30_Login(Extension of lesson29)

20.08.2024

## Flow:
1.  Create repository in GitHub and clone it to VScode
2.  Install all scripts(venv,flask,gunicorn,requirements.txt)
3.  Ask ChatGPT what is the best way to create DB
4.  Create and initialize DB
5.  Make all the packages(folder) and modules(file) and templates
6.  Make sure all code is good and commit it to GitHub
7.  Go to Render and create a new web service
8.  Create file .env(Environment Variables) and set a secret key(FLASK_SECRET_KEY = 1234)
9.  Create PostgreSQL on Render
10. Merge all scripts to postgres to new file (file name).py, create new end point function on app.py for psycopg2.connect,
    and fill the data of psycopg2.connect on files:( db.py & app.py )
11. Change all connections code on app.py 
    conn =sqlite3.connect("library.db") 
    <--> 
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

## Commands schema on VScode:
1.  ChatGPT: Plan a basic database schema for a library. Library has books, users. A user can loan a book for 10 days
2.  ChatGPT: Please create a python script for SQLite3, That will create this database and enter some rows of data for books, users, and loans
3.  python Data_Base/00_init.py
4.  python Data_Base/01_script.py
5.  python Data_Base/02_script.py
6.  python Data_Base/03_script.py
7.  python -m venv venv
8.  source venv/Scripts/activate
9.  pip install flask
10. pip install gunicorn 
11. pip install -r requirements.txt
12. pip install python-dotenv
    Merge all sprits to postgres:
13. ChatGPT: Copy and paste:(00_init,01_script,02_script,03_script),Write:Create a script from all this scripts for creating this database on render postgres
14. pip install psycopg2-binary
15. python Data_Base/04_postgres_db.py
16. python app.py

## Render:
Create a new repository in GitHub(Public)
Go to Render
New-->Web service-->Public Git Repository-->Enter GitHub URL(https://github.com/Sergey-Temkin/Lesson00.git)-->Connect

1.  Source Code: Sergey-Temkin/Lesson00
2.  Name: Lesson00
3.  Language: Python3
4.  Branch: main
5.  Region: Frankfurt(EU Central)
6.  Build Command: pip install -r requirements.txt
7.  Start Command: gunicorn app:app
8.  For hobby projects: Free
9.  Advanced-->Auto-Deploy: Yes
10. Deploy Web Service

After getting on Logs: Your service is live
Copy URL and print into web browser

## PostgreSQL(On Render)
New-->PostgreSQL
1. Name: Library00
2. Database: ---
3. User: ---
4. Region: Frankfurt(EU Central)
5. PostgreSQL Version: 16
6. Datadog API Key: ---
7. For hobby projects: Free
8. Create Database

## VScode path
PC:
cd "C:\Users\USER\OneDrive\Computer_Science/001-Code/001-Jhon-Bryce/000-GitHub/Lesson30_Login"
Laptop:
cd "C:\Users\sergh\OneDrive\Computer_Science/001-Code/001-Jhon-Bryce/000-GitHub/Lesson30_Login"

## Render
https://github.com/Sergey-Temkin/Lesson30_Login.git

## GIT
git add . 
git status 
git commit -m " " 
git push

git reset HEAD~1
git push -f origin main

python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
pip install flask
pip install flask-cors 
pip freeze 
deactivate

pip freeze > requirements.txt 
pip install -r requirements.txt

http://127.0.0.1:500
http://127.0.0.1:5500 