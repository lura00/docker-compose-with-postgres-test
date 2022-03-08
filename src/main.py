from fastapi import FastAPI, Depends, HTTPException, status
import psycopg2

app = FastAPI()

@app.on_event("startup")
def startup():
    app.db = psycopg2.connect("postgresql://test-breakingbad:testpass@db:5432/bbdb")

@app.on_event("shutdown")
def shutdown():
    app.db.close()


@app.get("/stores")
def stores():
    with app.db.cursor() as cur:
        cur.execute("SELECT id, name from stores")
        names = cur.fetchall()
        for name in names:
            return names

@app.get("/stores/adresses")
def stores():
    with app.db.cursor() as cur:
        cur.execute("SELECT id, store, address, zip, city from store_addresses")
        names = cur.fetchall()
        for name in names:
            return names