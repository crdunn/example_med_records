import pandas as pd

def get_db():
    return pd.read_csv("claims.csv")
def to_db(df):
    df.to_csv("claims.csv",index=False)

def get_claim_by_id(id):
    """
    This function accepts an integer and checks it against the values of claim_id in the database.
    Raises:
        TypeError if an int is not provided
        ValueError if there is no claim with that id
    """
    db = get_db()
    if id.isnumeric():
        claim = db.loc[db["claim_id"] == int(id)]
        if len(claim) == 1:
            return claim.to_dict(orient="records")
        else:
            raise ValueError("No such claim with that id")
    else: 
        raise TypeError("id must be an int")

def get_claims_by_name(name):
    """
    This function accepts a string and checks it against the values of patient_name in the database.
    Raises:
        TypeError if a string is not provided
        ValueError if there is no claim with that id
    """
    db = get_db()
    claim = db.loc[db["patient_name"] == name]
    if len(claim) == 1:
        return claim
    else:
        raise ValueError("No such patient with that name")


def get_claims_by_date(start,end,id = -1):
    """
    This function accepts a start date, and end date, and an optional patient id.  The dates should be in Year-Month-Day format, and the patient id should be an int
    Raises:
        ValueError if the dates are not in a correct format
        ValueError if 

    """
    db = get_db()
    try: 
        pd.to_datetime(start, format="%Y-%M-%d")
        pd.to_datetime(end, format="%Y-%M-%d")
        claims = db[(db["claim_date"] >= start) & (db["claim_date"] <= end)]
        if isinstance(id,int):
            if id > 0:
                claims = claims[claims["patient_id"] == id] 
        
            if len(claims) > 0: 
                return claims
            else:
                raise ValueError("No claims for that date range")
        else:
            raise TypeError("id must be an int")
       
    except ValueError:
        raise TypeError("Dates must be in Year-Month-Day format")

def add_claims(claims):
    """
    This function accepts a list of dictionaries that contain data that will be added to the database.
    Raises:
        TypeError: if a list of dictionaries is not provided
        ValueError if a dictionary's keys do not match the columns of the dataframe
    """
    if isinstance(claims,list):
        db = get_db()
        for claim in claims:
            if isinstance(claim,dict):
                row = pd.DataFrame(claim,index=[0])
                db = pd.concat([db,row],ignore_index=True)
            else:
                raise TypeError("Claims must be a list of dictionaries")
        to_db(db)
    else:
        raise TypeError("Claims must be a list of dictionaries")


def update_claim(id, claim):
    """
    TODO: Implement Update Claims function
    """
    pass

def delete_claim(id):
    """
    TODO: Implement Delete Claims function
    """

if __name__ == "__main__":
    print("db_utils.py")
    # print(get_claim_by_id(100))
    # print(get_claims_by_date("2023-11-01","2023-11-29",1))
    # print(get_claims_by_date("2023-11-01","2023-11-29","a"))
    # add_claims([{
    #     "claim_id":11,
    #     "patient_name":"John Doe",
    #     "patient_id":1,
    #     "claim_date":"2023-12-08",
    #     "patient_address":"123 Main St",
    #     "patient_city":"Cityville",
    #     "patient_state":"CA 90210",
    #     "insurance_provider":"Blue Shield",
    #     "service_code":"99213"
    # }])