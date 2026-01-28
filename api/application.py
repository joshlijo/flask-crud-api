from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
class Drink(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique = True, nullable = False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Drink": Drink}

@app.route("/")
def index():
    return "Hello!"

@app.route("/drinks", methods=["GET", "POST"], strict_slashes=False)
def drinks():
    if request.method == "GET":
        drinks = Drink.query.all()
        return {
            "drinks": [
                {"name": d.name, "description": d.description}
                for d in drinks
            ]
        }

    if request.method == "POST":
        data = request.get_json()
        drink = Drink(
            name=data["name"],
            description=data["description"]
        )
        db.session.add(drink)
        db.session.commit()
        return {
            "id": drink.id,
            "name": drink.name,
            "description": drink.description
        }, 201

@app.route('/drinks/<int:id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return {"name": drink.name, "description": drink.description}

@app.route('/drinks/<int:id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {"error": "not found"}
    db.session.delete(drink)
    db.session.commit()
    return {"message": "yeet!"}