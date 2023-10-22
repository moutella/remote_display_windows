from controllers.display import get_config_mock, save_config
from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from controllers.monitor import DisplayHelper

app = FastAPI()

display = DisplayHelper()


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


@app.get("/display/config/")
@app.get("/display/config/{rdrc_id}")
def get_config(rdrc_id: int = None):
    """Returns"""
    print(rdrc_id)
    if rdrc_id is not None:
        print(rdrc_id)
        config = display.get_hardware_config(rdrc_id)
        if config:
            return config
        else:
            raise HTTPException(status_code=404, detail="Could not find monitor")
    return display.get_config()


class Monitor(BaseModel):
    rdrc_id: int = None
    logical_name: str = None


@app.delete("/display/")
def disable_monitor(RDRC: Monitor):
    print(RDRC)
    rdrc_id = RDRC.rdrc_id
    config = display.get_hardware_config(rdrc_id)
    print(config)
    if config:
        display.disable_monitor(config["logical_name"])
    else:
        raise HTTPException(status_code=404, detail="Could not find monitor")


class MonitorConfig(BaseModel):
    rdrc_id: int = None
    logical_name: str = None
    width: int = 1920
    height: int = 1080
    refresh_rate: int = 60
    position_x: int = None
    position_y: int = None
    active: bool = False


@app.post("/display/")
def enable_monitor(Config: MonitorConfig):
    logical_name = Config.logical_name
    if logical_name:
        display.set_display_config(
            Config.logical_name,
            Config.width,
            Config.height,
            Config.refresh_rate,
            Config.position_x,
            Config.position_y,
            Config.active,
        )
    else:
        raise HTTPException(status_code=404, detail="Could not find monitor")
