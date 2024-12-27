from fastapi import FastAPI
from app.models import Patient  # Importing the Patient model
from typing import List

app = FastAPI()

# In-memory database for demonstration
patients = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the Patient Service API"}

@app.post("/patients/")
def create_patient(patient: Patient):
    patients.append(patient)
    return {"message": "Patient added successfully", "patient": patient}

@app.get("/patients/")
def get_patients():
    return {"patients": patients}
