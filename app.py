from flask import Flask, request, jsonify
from flask_sqlalchemy importSQLAlchemt
from flask_marshmallow import flask_marshmallow
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Todo(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.string(100), nullable=False)
    done = db.Column(db.Boolean)

    def __init__(self, title, done)
    self.title = title
    self.done = done

    class TodoSchema(ma.Schema):
        class Meta:
            fields = ("id", "title", "done")

todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)

@app.route("/", methods=["GET"])
def home():
    return "<h1>Todo Flask API</h1>"

if __name__ == "__main__":
    app.run(debug=True)