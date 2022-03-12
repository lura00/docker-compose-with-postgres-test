from fastapi import FastAPI, HTTPException, status
import psycopg2
import psycopg2.extras

app = FastAPI()


conn = psycopg2.connect("postgresql://test-breakingbad:testpass@db:5432/bbdb")
cur  = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


@app.on_event("shutdown")
def shutdown():
    conn.close()


@app.get("/")
def root():
    return("WELCOME TO BRAKING BAD")


# Test codes:
# lt = [('Geeks', 2), ('For', 4), ('geek', '6')]
  
# # using list comprehension
# out = [item for t in lt for item in t]

# "SELECT name, string_agg(address || '' || zip || '' ||city, '')  FROM stores JOIN store_addresses on store = stores.id group by name"
# Docker image prune

# Imports for schema.py:
# from typing import Optional
# from typing import List
# from . import schema


@app.get("/stores")
async def stores():

    cur.execute("SELECT name, store_addresses.address, store_addresses.zip, store_addresses.city FROM stores JOIN store_addresses on store = stores.id")
    stores = cur.fetchall()

    return {"data": stores}


@app.get("/stores/{name}")
async def read_item(name: str):

    cur.execute("SELECT stores.name, store_addresses.address FROM stores JOIN store_addresses ON stores.id=store_addresses.store WHERE name=(%s)", (name,))
    data = cur.fetchall()

    if len(data) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No stores was found")
    
    return {"data": data}


@app.get("/city/{city}")
async def get_city(city: str):

    zip = city
    cur.execute("SELECT city FROM store_addresses WHERE city= (%s) OR zip= (%s)", (city, zip))
    data = cur.fetchall()

    if len(data) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No stores was found")

    return {"data": data}
