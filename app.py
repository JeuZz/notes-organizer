from flask import Flask, render_template, request, redirect
import json, os

app = Flask(__name__)

NOTES_FILE = "notes.json"

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            return json.load(f)
    return {}

def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=4)

@app.route("/")
def index():
    notes = load_notes()
    return render_template("index.html", notes=notes)

@app.route("/add", methods=["POST"])
def add_note():
    note = request.form["note"]
    category = request.form["category"]
    notes = load_notes()
    notes.setdefault(category, []).append(note)
    save_notes(notes)
    return redirect("/")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
