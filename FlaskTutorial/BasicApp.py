# This is basic demo app for flask 
from flask import Flask,request

app = Flask(__name__)


@app.route('/')
def index():
    return 'This is homepage'

# @ when user ask for URL ,then decorator return what ever at return value


@app.route('/AboutUs')
def hello():
    return 'Hello, World'


if __name__ == '__main__':  # It will run only when it will call directly
    app.run(debug=True)     # Start this app at local web server 
    
# If there is no main method on the app then run these two command in the terminal a) set FLASK_APP=app.py b)flask run    
# When you will execute this basic app you will see these lines on the terminal    
# Click on the http://127.0.0.1:5000/ and Homepage will open with this line This is homepage
# If you run http://127.0.0.1:5000/AboutUs then you will get Hello, World
"""
 C:\Program Files (x86)\Python35-32\python3.exe" D:/DemoProject/Flask/app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 131-398-135
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [13/Nov/2018 14:31:30] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [13/Nov/2018 14:31:31] "GET /favicon.ico HTTP/1.1" 404 -
 * Detected change in 'D:\\DemoProject\\Flask\\app.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 131-398-135
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
"""    
    
