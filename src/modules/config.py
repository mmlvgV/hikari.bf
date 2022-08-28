import ujson

with open("./src/options.json", "r") as options:
    data = ujson.load(options)

TOKEN = data["token"]
PREFIX = data["prefix"]
