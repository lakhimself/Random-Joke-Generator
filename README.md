

---
# 🎭 Random Joke Generator – CLI & Web App
````markdown
A lighthearted project that delivers jokes straight from the [JokeAPI](https://jokeapi.dev/) in two flavors:
- 🖥️ A command-line interface (CLI) for terminal laughs
- 🌐 A web-based app** using Flask, JavaScript, and Tailwind CSS

Choose your style, pick a category, and get ready to laugh!

## 🤹 Introduction

Continuous Joke Generator is a fun and interactive Python project that lets you fetch jokes in real-time using the JokeAPI. It comes in two versions:
- CLI version: Ideal for quick terminal laughs. You choose the category and keep getting jokes until you type "stop".
- Web version: A Flask-powered app with Tailwind CSS and JavaScript to deliver jokes dynamically in your browser.

## ✨ Features

- 🎯 Select from multiple joke categories: `Any`, `Programming`, `Misc`, `Pun`, `Spooky`, `Christmas`
- 😂 Handles both single-line and two-part jokes
- 🔁 CLI loop or dynamic web UI for non-stop jokes
- ⚡ Interactive, responsive, and fast
- 🌈 Styled with Tailwind CSS (Web version)

````
### 1. Clone the Repository

```bash
git clone https://github.com/lakhimself/joke-generator.git
cd joke-generator
````

### 2. Set Up a Python Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Required Dependencies

```bash
pip install flask requests
```

---

## 🚀 Usage

### ▶️ CLI Mode

Navigate to the folder containing `cli_jokes.py` (or similar script name):

```bash
python cli_jokes.py
```

You’ll be prompted to enter a joke category and press Enter to get new jokes. Type `stop` to exit.

### 🌐 Web App Mode

Run the Flask server:

```bash
python app.py
```

Open your browser and go to:
`http://127.0.0.1:5000`

Click the “Get Joke” button to dynamically fetch jokes from the API.

---

## 📂 Project Structure

```
joke_generator/
│
├── app.py               # Flask backend for web app
├── cli_jokes.py         # CLI-based joke generator
├── templates/
│   └── index.html       # HTML frontend with Tailwind CSS
├── static/
│   └── script.js        # JavaScript to call /joke endpoint
└── requirements.txt     # Python dependencies (optional)
```

---

## 📦 Dependencies

* [`Flask`](https://palletsprojects.com/p/flask/)
* [`Requests`](https://pypi.org/project/requests/)

Install with:

```bash
pip install flask requests
```

---

## ⚙️ Configuration

No extra config needed.

If you'd like to modify:

* **Joke category**: Adjust the URL in `app.py` or CLI script
* **Styling**: Modify `index.html` and use [Tailwind CSS](https://tailwindcss.com/)
* **Endpoints**: Extend Flask routes in `app.py`

---

## 💡 Examples

### CLI Output

```
🎭 Welcome to the Continuous Joke Generator 🎭
Type 'stop' at any time to end.

Enter joke category (Any, Programming, Misc, Pun, Spooky, Christmas): Programming
Press Enter to get a joke or type 'stop' to quit:

--- Here's your joke ---

Why do programmers prefer dark mode?

(Press Enter for punchline...)

Because light attracts bugs.
```

### Web UI Output

```text
[Browser view]

Click "Get Joke" to receive:
🗨️ Why did the chicken join a band?
🥁 Because it had the drumsticks!
```

---

## 🧯 Troubleshooting

| Problem                 | Solution                          |
| ----------------------- | --------------------------------- |
| Page loads but no jokes | Check Flask server and JS console |
| ModuleNotFoundError     | Run `pip install flask requests`  |
| 404 or fetch failure    | Ensure Flask server is running    |
| No jokes in CLI         | Check internet connection         |

