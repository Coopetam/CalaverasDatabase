from flask import Flask, render_template
from calaverasstorage import load_characters

app = Flask(__name__)


def get_character_by_name(name):
    characters = load_characters()
    for char in characters:
        if char.name == name:
            return char
    return None


@app.route("/")
def home():
    characters = load_characters()
    return render_template("admin_dashboard.html", characters=characters)


@app.route("/character/<name>")
def view_character(name):
    character = get_character_by_name(name)

    if not character:
        return "Character not found", 404

    return render_template("calaverassheet.html", character=character)


if __name__ == "__main__":
    app.run(debug=True)