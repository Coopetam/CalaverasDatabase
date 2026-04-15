from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "calaveras-secret"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calaveras.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    player = db.Column(db.String(100))
    heritage = db.Column(db.String(50))
    profession = db.Column(db.String(50))
    notes = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

def get_character_by_name(name):
    return Character.query.filter_by(name=name).first()


@app.route("/")
def home():
    return redirect(url_for("admin_characters"))

@app.route("/admin/characters")
def admin_characters():
    characters = Character.query.all()
    return render_template("admin_characters.html", characters=characters)

@app.route("/character/<int:id>")
def view_character(id):
    character = Character.query.get_or_404(id)
    return render_template("calaverassheet.html", character=character)

if __name__ == "__main__":
    app.run(debug=True)