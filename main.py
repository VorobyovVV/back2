from http.client import HTTPException
from typing import Union, List
from fastapi import FastAPI
from pydantic import BaseModel
from starlette import status

import models
from database import SessionLocal

app = FastAPI()

class Car(BaseModel):
    id:int
    producer:str
    model:str
    owner:str
    releaseYear:int
    color:str
    MaxSpeed:int
    image:int
    name:str
    description:str
    price:int
    on_offer:bool


class Config:
    orm_mode = True


db = SessionLocal()


@app.get('/car', response_model=List[Car], status_code=200)
def get_all_car():
    car = db.query(models.car).all()

    return car


@app.get('/car/{car_id}', response_model=Car, status_code=status.HTTP_200_OK)
def get_an_car(car_id: int):
    car = db.query(models.car).filter(models.car.id == car_id).first()
    return car


@app.post('/car', response_model=Car,
          status_code=status.HTTP_201_CREATED)
def create_an_car(car: Car, new_car=None):
    db_car = db.query(models.car).filter(models.car.name == car.name).first()

    if db_car is not None:
        raise HTTPException(status_code=400, detail="Item already exists")

    new_item = models.car(
        name=car.name,
        price=car.price,
        description=car.description,
        on_offer=car.on_offer
    )

    db.add(new_car)
    db.commit()

    return new_car


@app.put('/car/{car_id}', response_model=Car, status_code=status.HTTP_200_OK)
def update_an_item(car_id: int, car: Car):
    car_to_update = db.query(models.car).filter(models.car.id == car_id).first()
   # car_to_update.name = car.name
   # car_to_update.price = car.price
   # car_to_update.description = car.description
   # car_to_update.on_offer = car.on_offer

    db.commit()

    return car_to_update


@app.delete('/car/{car_id}')
def delete_item(car_id: int, car_to_delete=None):
    item_to_delete = db.query(models.car).filter(models.car.id == car_id).first()

    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource Not Found")

    db.delete(car_to_delete)
    db.commit()

    return car_to_delete