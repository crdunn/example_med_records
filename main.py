from flask import Flask, jsonify
import db_utils as db

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/patient/id/<id>")
def get_claim_by_id(id):
    try:
        claims = db.get_claim_by_id(id)
        return jsonify(claims)
    except ValueError as e:
        return str(e)
    except TypeError as e:
        return str(e)

@app.route("/patient/name/<name>")
def get_claims_by_name(name):
    try:
        claims = db.get_claims_by_name(name)
        return jsonify(claims)
    except ValueError as e:
        return str(e)
    except TypeError as e:
        return str(e)

@app.route("/user/<start>/<end>")
@app.route("/user/<start>/<end>/<id>")
def get_claims_by_date(start,end,id=-1):
    try:    
        claims = db.get_claims_by_date(start,end,id)
        return jsonify(claims)
    except ValueError as e:
        return str(e)
    except TypeError as e:
        return str(e)


if __name__ == "__main__":
    app.run(debug=True)