from fastapi import FastAPI,HTTPException
import csv
import os
from app.model.employee import Employee
from app.service._emp___ import __emp,lifespan

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"Hello": "World"}




# 5. The API endpoint to add an employee automatically to the CSV
@app.post("/add-employee/")
async def add_employee(employee: Employee):
    return __emp.save(employee)

# 6. The API endpoint to Fetch Frist 5 employee automatically into the CSV
@app.get("/fetch-employees/")
async def fetch_employee():
    return __emp._getemp()


@app.get("/fetch-employee/{id}")
async def fetch_employee(id:int):
    return __emp._getemp(id) 


