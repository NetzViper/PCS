#!/usr/bin/env python3
# server.py: Backend for MyCamServ
# Author: Luna
# Version: v0.0.1
# Date: 15.02.2022

from flask import Flask, render_template
from os import urandom

from methods import load_config

app = Flask(__name__)
app.config["SECRET_KEY"] = urandom(31)
app.config["CONFIG"] = load_config()


@app.route("/", methods=["GET"])
def GET_index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host=app.config["CONFIG"]["server"]["host"], port=app.config["CONFIG"]["server"]["port"], debug=app.config["CONFIG"]["server"]["debug"])