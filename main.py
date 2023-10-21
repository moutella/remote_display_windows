from controllers.display import get_config_mock, save_config
from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Returns Custom Monitor Config"""
    return {"Hello": "World", "monitor": get_config_mock()}


@app.get("/config/save/{monitor_id}")
def save_display_config(monitor_id: int):
    save_config()
    return True


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/resolution")
def get_config(item_id: int = None):
    """Returns"""
    print(item_id)
    displays = []

    return {"displays": displays}


@app.post("/resolution")
def set_resolution(item_id: int = None):
    print(item_id)
