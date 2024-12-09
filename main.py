from flask import Flask, jsonify
import db_utils as db

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/patient/<id>")
def get_claim_by_id(id):
    claim = db.get_claim_by_id(id)
    print(claim)
    return jsonify(db.get_claim_by_id(id))

if __name__ == "__main__":
    app.run(debug=True)