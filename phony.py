#!/usr/bin/env python3
from discord import Client
from json import load

with open(".bottoken") as f:
    token = f.read()

client = Client()

client.run(token)
