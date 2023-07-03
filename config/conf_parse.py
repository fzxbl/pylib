import toml
import os
from types import *

from env import CONF_DIR

def load_toml_config(conf_name:str) -> any:
    cfg = toml.load(os.path.join(CONF_DIR, conf_name))
    return cfg


if __name__ == '__main__': 
    cfg = load_toml_config('stockauth.toml')
    print(cfg)