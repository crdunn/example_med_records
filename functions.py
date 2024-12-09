import pandas as pd

def get_db():
    return pd.read_csv("claims.csv")

def get_claim_by_id(id):
    pass

def get_claims_by_name(name):
    pass

def get_claims_by_date(start,end,id = -1):
    pass

def add_claim(claim):
    pass

def add_claims(claims):
    pass

def update_claim(id, claim):
    pass

def delete_claim(id):
    pass