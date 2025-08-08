import requests

def get_joke(category="Any"):
    url = f"https://v2.jokeapi.dev/joke/{category}?format=json"
    try:
        response = requests.get(url)
        data = response.json()

        if data["error"]:
            print("Oops! Couldn't fetch a joke.")
            return

        print("\n--- Here's your joke ---\n")
        if data["type"] == "single":
            print(data["joke"])
        else:
            print(data["setup"])
            input("\n(Press Enter for punchline...)\n")
            print(data["delivery"])
        print("\n------------------------\n")

    except Exception as e:
        print("Something went wrong:", e)

def start_joke_loop():
    print("🎭 Welcome to the Continuous Joke Generator 🎭")
    print("Type 'stop' at any time to end.\n")
    category = input("Enter joke category (Any, Programming, Misc, Pun, Spooky, Christmas): ").title()
    if category == "":
        category = "Any"

    while True:
        command = input("Press Enter to get a joke or type 'stop' to quit: ").strip().lower()
        if command == "stop":
            print("👋 Okay, no more jokes. Have a great day!")
            break
        get_joke(category)

if __name__ == "__main__":
    start_joke_loop()
