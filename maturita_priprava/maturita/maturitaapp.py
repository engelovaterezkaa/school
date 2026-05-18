from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/formular")
def formular():
    name = request.args.get("name")
    print(name)
    return render_template("formular.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)