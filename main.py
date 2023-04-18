from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Worldwwwwwwwwwwwwwwwww"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": 3, "q": "kaka3434343433434"}

@app.get("/countries/{country}")
async def get(country:str):

    return {"message": country}