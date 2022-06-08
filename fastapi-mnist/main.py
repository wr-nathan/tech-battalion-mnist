"""Entrypoint for prediction API."""
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Get application root hello world message."""
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    """Get item from given ID."""
    return {"item_id": item_id, "q": q}
