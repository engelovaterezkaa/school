from flask import Flask, render_template, redirect, url_for, request, g
import json
import os

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/contact")
def contact():
    email = request.args.get("email")
    message = request.args.get("message")
    if email and message:
        print(email, message) 
        data ={ 
            "Email": email,
            "Message": message
            }
        
        print(data)

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

    return render_template("contact.html")

@app.route("/manual")
def manual():
    email = request.args.get("jinja_email", default="___")
    message = request.args.get("jinja_message", default="___")

    return render_template("manual.html", jinja_email=email, jinja_message=message)


if __name__ == "__main__":
    app.run(debug=True)