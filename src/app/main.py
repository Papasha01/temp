from typing import Annotated
from pydantic import BaseModel, Field
from fastapi import FastAPI, Query
import subprocess

import time

app = FastAPI()

counter = 999

@app.get("/get_num/")
async def get_num():
    global counter
    counter+=1
    while ps(counter) == True:
        print(counter)
        counter += 1
    return counter

@app.post("/set_num/")
async def set_num(num: Annotated[int, Query(gt=0, lt=10000)]):
    global counter
    counter = num


def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed

def ps(num):
    command = f'Get-ADComputer -Identity "klimovpc{num}"'
    ps_info = run(command)
    if ps_info.returncode != 0:
        return False
    else:
        return True
