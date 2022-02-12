from flask import Flask #, request, render_template, redirect, session
import socket

app = Flask(__name__)
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

@app.route("/")
def index():
    return local_ip


if (__name__ == "__main__"):
        app.run(debug=True)
