from fastapi import FastAPI
from pydantic import BaseModel
from database import DBConnect
from fastapi.encoders import jsonable_encoder



class ReadOrDelete(BaseModel):
    name: str

class CreateOrUpdate(BaseModel):
    name: str
    birthday: str

application = app = FastAPI()



@app.post("/create")
async def feature(item: CreateOrUpdate):

    request = jsonable_encoder(item)
    name = request["name"]
    birthday = request["birthday"]
    dbconn = DBConnect()
    response = dbconn.add_birthday(name, birthday)
    return response


@app.post("/read")
async def feature(item: ReadOrDelete):

    request = jsonable_encoder(item)
    name = request["name"]
    dbconn = DBConnect()
    response = dbconn.read_birthday(name)
    return response

    
@app.post("/update")
async def feature(item: CreateOrUpdate):

    request = jsonable_encoder(item)
    name = request["name"]
    new_birthday = request["birthday"]
    dbconn = DBConnect()
    response = dbconn.update_birthday(name, new_birthday)
    return response
    
@app.post("/delete")
async def feature(item: ReadOrDelete):

    request = jsonable_encoder(item)
    name = request["name"]
    dbconn = DBConnect()
    response = dbconn.delete_birthday(name)
    return response