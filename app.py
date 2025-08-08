from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/joke")
def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any?format=json"
    response = requests.get(url)
    data = response.json()

    if data["error"]:
        return jsonify({"error": True, "message": "Couldn't fetch a joke."})

    if data["type"] == "single":
        return jsonify({"joke": data["joke"], "type": "single"})
    else:
        return jsonify({"setup": data["setup"], "delivery": data["delivery"], "type": "twopart"})

if __name__ == "__main__":
    app.run(debug=True)
