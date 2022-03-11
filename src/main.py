from unittest import result
from fastapi import FastAPI, HTTPException, status
from typing import Optional
import psycopg2

app = FastAPI()

# conn = None
# @app.on_event("startup")
# def startup():
conn = psycopg2.connect("postgresql://test-breakingbad:testpass@db:5432/bbdb")
# cur = conn.cursor()

@app.on_event("shutdown")
def shutdown():
    conn.close()


@app.get("/")
def root():
    return("WELCOME TO BRAKING BAD")


# lt = [('Geeks', 2), ('For', 4), ('geek', '6')]
  
# # using list comprehension
# out = [item for t in lt for item in t]

@app.get("/stores")
def stores():
    with conn.cursor() as cur:
        cur.execute("SELECT name FROM stores")
        stores = cur.fetchall()
        cur.execute("SELECT address, zip, city FROM store_addresses")
        addresses = cur.fetchall()
        
        store_list = [item for t in stores for item in t]
        address_list = [item for t in addresses for item in t]

        results = {"Namn": str(store_list[0]), "Address": str(address_list[0]), "zip": str(address_list[1]), "city": str(address_list[2])}
        return {"data": [results]}

# "SELECT name, string_agg(address || '' || zip || '' ||city, '')  FROM stores JOIN store_addresses on store = stores.id group by name"
# Docker image prune

@app.get("/stores/{name}")
async def read_item(name: str):
    with conn.cursor() as cur:
        cur.execute("SELECT stores.name, store_addresses.address FROM stores JOIN store_addresses ON stores.id=store_addresses.store WHERE name=(%s)", (name,))
        data = cur.fetchone()
        # data_list = [item for t in data for item in t]
        if data == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No stores was found")
        
        return {"data": data}


# @app.get("/cities")
# async def get_cities():
#     with conn.cursor() as cur:
#         cur.execute("SELECT DISTINCT city FROM store_addresses")
#         data = cur.fetchall()
#         data_list = [item for t in data for item in t]
#         if data == None:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No stores was found")

#         return {"data": data_list}


@app.get("/{city}")
async def get_city(city: str):
    with conn.cursor() as cur:
        zip = city
        cur.execute("SELECT city FROM store_addresses WHERE city= (%s) OR zip= (%s)", (city, zip))
        data = cur.fetchall()
        data_list = [item for t in data for item in t]
        if len(data_list) == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No stores was found")
        else:
            return {"data": data_list}
