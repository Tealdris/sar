from typing import Union

from fastapi import FastAPI
import datetime

time = {
    "Hello world! Time is: ": datetime.datetime.now()
}

app = FastAPI()

@app.get("/")
def read_root():
    return time
