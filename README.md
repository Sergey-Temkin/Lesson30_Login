## Lesson30_Login(Extension of lesson29)

20.08.2024-

# Flow:
1.  Create repository in GitHub and clone it to VScode
2.  Install all scripts(venv,flask,gunicorn,requirements.txt)
3.  Ask ChatGPT what is the best way to create DB
4.  Create and initialize DB
5.  Make all the packages(folder) and modules(file) and templates
6.  Make sure all code is good and commit it to GitHub
7.  Go to Render and create a new web service


# Commands schema on VScode:
1.  Plan a basic database schema for a library. Library has books, users. A user can loan a book for 10 days(ChatGPT)
2.  Please create a python script for SQLite3, That will create this database and enter some rows of data for books, users, and loans(ChatGPT)
3.  python Data_Base/00_init.py
4.  python Data_Base/01_script.py
5.  python Data_Base/02_script.py
6.  python -m venv venv
7.  source venv/Scripts/activate
8.  pip install flask
9.  pip install gunicorn 
10. pip install -r requirements.txt

# Render:
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

# VScode path
cd "C:\Users\sergh\OneDrive\Computer_Science/001-Code/001-Jhon-Bryce/000-GitHub/Lesson30_Login"
cd "C:\Users\USER\OneDrive\Computer_Science/001-Code/001-Jhon-Bryce/000-GitHub/Lesson30_Login"

# Render
https://github.com/Sergey-Temkin/Lesson30_Login.git


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

python app.py

http://127.0.0.1:500
http://127.0.0.1:5500 