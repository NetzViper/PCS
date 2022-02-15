#!/usr/bin/env python3
# server.py: Methods for MyCamServ backend
# Author: Luna
# Version: v0.0.1
# Date: 15.02.2022

import json

def load_config() -> dict:
    try:
        return json.load(open("config.json", "r"))
    except:
        raise FileNotFoundError("Config file does not exist")