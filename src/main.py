from fastapi import FastAPI, Depends, HTTPException, status
import psycopg2

app = FastAPI()

@app.on_event("startup")
def startup():
    app.db = psycopg2.connect("postgresql://test-breakingbad:testpass@db:5432/bbdb")
    #app.db = psycopg2.connect("postgresql://postgres:1234@localhost:5432/bbdb")

@app.on_event("shutdown")
def shutdown():
    app.db.close()


@app.get("/stores")
async def stores():
    with app.db.cursor() as cur:

        cur.execute("SELECT id, name from stores")
        names = cur.fetchall()
        return names

@app.get("/stores/adresses")
def stores():
    with app.db.cursor() as cur:
        cur.execute("SELECT id, store, address, zip, city from store_addresses")
        names = cur.fetchall()
        return list(names)

@app.get("/")
def root():
    return("WELCOME TO BRAKING BAD")

@app.get("/stores/{name}")
async def read_item(name: str):
    with app.db.cursor() as cur:
        cur.execute("SELECT name FROM stores WHERE name=(%s)", (name,))
        names = cur.fetchall()
        if (name,) not in names:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No stores was found")
        else:
            return name