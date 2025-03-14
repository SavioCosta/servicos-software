from typing import Optional, Union
from fastapi import FastAPI, FIle, Upload

import json from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def diz_ola():
    return {"Ola":"Mundo"}