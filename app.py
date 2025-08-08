from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/joke")
def get_joke():
    category = request.args.get("category", "Any")
    url = f"https://v2.jokeapi.dev/joke/{category}?format=json"
    response = requests.get(url)
    data = response.json()

    if data["error"]:
        return jsonify({"error": True, "message": "Couldn't fetch a joke."})

    if data["type"] == "single":
        return jsonify({"joke": data["joke"], "type": "single", "category": data["category"]})
    else:
        return jsonify({
            "setup": data["setup"],
            "delivery": data["delivery"],
            "type": "twopart",
            "category": data["category"]
        })

if __name__ == "__main__":
    app.run(debug=True)
