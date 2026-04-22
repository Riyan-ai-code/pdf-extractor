#1
from fastapi import FastAPI
import schema
app=FastAPI()

@app.get('/')
def start():
    return {"message":"app started"}
@app.post('/pdf')
def pdf(request:schema.pdf):
    return {"messsage":"pdf"}