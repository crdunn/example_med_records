from flask import Flask, jsonify,request
import db_utils as db

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the example medical records system"

@app.route("/")
def all_claims():
    return jsonify(db.get_all_claims())

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
    
@app.route("/doctor/claim",methods=["POST"])
def upload_claims():
    if request.method == "POST":
        try:
            claims = request.json
            db.add_claims(claims)
        except TypeError as e:
            return str(e)
        except ValueError as e:
            return str(e)



if __name__ == "__main__":
    app.run(debug=True)