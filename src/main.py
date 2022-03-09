from fastapi import FastAPI, Depends, HTTPException, status
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
   return {"message": "Welcome to a Kjell-production"}


@app.get("/stores")
def stores():
    with conn.cursor() as cur:
        cur.execute("SELECT * from stores")
        data = cur.fetchall()
      
        return data


@app.get("/stores/{name}")
async def read_item(name: str):
    with conn.cursor() as cur:
        cur.execute("SELECT stores.name, store_addresses.address FROM stores JOIN store_addresses ON stores.id=store_addresses.store WHERE name=(%s)", (name,))
        data = cur.fetchone()
        if data == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No stores was found")
        
        return data


@app.get("/cities")
async def get_cities():
    with conn.cursor() as cur:
        cur.execute("SELECT DISTINCT city FROM store_addresses")
        data = cur.fetchall()

        if data == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No stores was found")

        return data


@app.get("/city/{zip}")
async def get_city(zip: str):
    with conn.cursor() as cur:
        cur.execute("SELECT city FROM store_addresses WHERE zip = (%s)", (zip,))
        data = cur.fetchone()

        if data == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No stores was found")
        else:
            return data