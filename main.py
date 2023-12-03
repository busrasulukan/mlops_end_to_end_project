from fastapi import FastAPI
import pickle
import pandas as pd
from pydantic import BaseModel

#Get => Select
#Post => Insert
#Put => Update
#Delete => Delete

app = FastAPI()

@app.get("/") #Web sitesinin ilk açılan sayfasıdır /  /index /home
def home():
    return("Churn Prediction API'nın ilk versiyonuna hoş geldiniz.")


class logreg_scheme(BaseModel):
    gender: int
    Partner: int
    Dependents: int
    tenure: int
    PhoneService: int
    PaperlessBilling: int
    MonthlyCharges: float
    TotalCharges: float
    NEW_AVG_Charges: float
    NEW_Increase: float
    NEW_AVG_Service_Fee: float
    

@app.post("/predict/logistic_regression/")
def make_predict(predict_values: logreg_scheme):
    loaded_model = pickle.load(open("logistic_regression_model.pkl", "rb"))
    df = pd.DataFrame([predict_values.dict().values()], columns=predict_values.dict().keys())
    predict = loaded_model.predict(df)
    return {"Predict": int(predict[0])}

