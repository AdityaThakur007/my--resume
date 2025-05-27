from flask import Flask, send_file
import os
&nbsp;
&nbsp;

app = Flask(__name__)
&nbsp;
&nbsp;

@app.route("/")
def home():
    # Send resume.html file as response
    return send_file(os.path.join(os.path.dirname(__file__), "..", "resume.html"))
&nbsp;
&nbsp;

def handler(environ, start_response):
    return app(environ, start_response)