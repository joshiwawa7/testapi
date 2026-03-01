from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to my firt FastAPI application!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return{"item_id": item_id, "query":q}

@app.get("/multiply/{a}/{b}")
async def multiply(a: int, b: int):
    result = a * b
    return{"result": result}