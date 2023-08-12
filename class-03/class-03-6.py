import tomllib
from rich import print

with open("/Users/m/Projects/python-for-everybody/class-03/input.toml", "rb") as file:
    data = tomllib.load(file)

print(data)