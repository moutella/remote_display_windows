import json
from models.display import DisplayConfig


def get_config_mock():
    config = DisplayConfig(1920, 1080, 60, 0, 0, "Display 1", "LG123")
    return config


def save_config():
    config = DisplayConfig(1920, 1080, 60, 0, 0, "Display 1", "LG1234")
    print(config)
    print(config.__dict__)
    config = json.dump(config.__dict__, open("teste.json", "w+"))
    print(config)
    return True
