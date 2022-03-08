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
        return list(names)

@app.get("/")
def root():
   return {"message": "Welcome to a Kjell-production"}


@app.get("/stores/{name}")
async def read_item(name: str):
    with app.db.cursor() as cur:
        hej = cur.execute("SELECT * FROM stores WHERE name = %s", (name,))
        data = cur.fetchall()
        if not data in hej:
            print("Hejdå")            
            #raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details="No stores was found")
        return list(data)



#SLASK
#@app.get("/stores/{name}")
#async def read_item(name: str): 
#    with app.db.cursor() as cur:
#        cur.execute("SELECT {name} FROM stores")
#        names = cur.fetchall()
#        if name == "":
#            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details="No stores was found")
#        return list{"name":name}


#c.execute('SELECT * FROM stocks WHERE symbol=?', t)
