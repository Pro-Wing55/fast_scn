import csv
import os
import pandas as pd
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException

from pydantic import BaseModel
from app.model.employee import Employee

# 1. Define the CSV file path and layout
CSV_FILE_PATH = "app/employees.csv"
CSV_HEADERS = ["ID", "Name", "Role", "City","Salery"]

# 2. Define the Lifespan event to create the file on startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    # This code runs exactly when the program starts up
    if not os.path.exists(CSV_FILE_PATH):
        with open(CSV_FILE_PATH, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(CSV_HEADERS)  # Write the top header row
        print(f"🎉 Created new tracking file: {CSV_FILE_PATH}")
    else:
        print(f"📁 Found existing tracking file: {CSV_FILE_PATH}")
        
    yield  # The application serves requests here
    
    # Optional: Any code placed here runs when the program shuts down
    print("👋 Shutting down server...")



class __emp():

    def _getemp():
          # 1. Load the CSV into a DataFrame
         df = pd.read_csv(CSV_FILE_PATH)
         return df.to_dict(orient="records")

    
    def _getemp(id):
              # 1. Load the CSV into a DataFrame
            df = pd.read_csv(CSV_FILE_PATH)

            felterDf=df[df['ID']==id]
              # 3. Check if the employee exists
            if felterDf.empty:
                raise HTTPException(status_code=404, detail=f"Employee with ID {id} not found.")
                
            # 4. Convert only the first matched row to a clean dictionary and return it
            return felterDf.to_dict(orient="records")[0]
             

    

    def save(employee:Employee):
        try:
                # Open the file in 'a' (append) mode so we don't overwrite previous records
                with open(CSV_FILE_PATH, mode="a", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                
                    # Write the employee values row by row
                    writer.writerow([
                        employee.id,
                        employee.name,
                        employee.age,
                        employee.city,
                        employee.salery
                    ])
                    
                return {
                    "status": "success",
                    "message": f"Employee {employee.name} added to CSV automatically!"
                }
                
        except Exception as e:
                
                raise HTTPException(status_code=500, detail=f"Failed to write to file: {str(e)}")




