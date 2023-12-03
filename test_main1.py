from fastapi.testclient import TestClient
from main import app

client =TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_logreg_predict():
    data = {
    "gender": 0,
    "Partner": 1,
    "Dependents": 1,
    "tenure": 0,
    "PhoneService": 1,
    "PaperlessBilling": 0,
    "MonthlyCharges": 29.85,
    "TotalCharges": 29.85,
    "NEW_AVG_Charges": 14.925,
    "NEW_Increase": 0.5,
    "NEW_AVG_Service_Fee":14.925
    }

data = {
    "gender": 0,
    "Partner": 1,
    "Dependents": 1,
    "tenure": 0,
    "PhoneService": 1,
    "PaperlessBilling": 0,
    "MonthlyCharges": 29.85,
    "TotalCharges": 29.85,
    "NEW_AVG_Charges": 14.925,
    "NEW_Increase": 0.5,
    "NEW_AVG_Service_Fee":14.925
    }
response = client.post("/predict/logistic_regression/", json = data)

assert response.status_code == 200