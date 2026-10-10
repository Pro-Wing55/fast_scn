from pydantic import BaseModel

class Employee(BaseModel):
      
      name:str
      id:int
      age:int
      city:str
      salery:int   