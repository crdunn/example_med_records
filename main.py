from flask import Flask, jsonify
import db_utils as db

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/patient/<id>")
def get_claim_by_id(id):
    try:
        claims = db.get_claim_by_id(id)
        return jsonify(claims)
    except ValueError as e:
        return str(e)
    except TypeError as e:
        return str(e)


if __name__ == "__main__":
    app.run(debug=True)