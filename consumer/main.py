"""Consume greetlib from GitHub Packages."""

from greetlib import greet, greet_many

print(greet("Alice"))
print(greet("Bob", "Howdy"))
print(greet_many(["X", "Y", "Z"], greeting="Yo"))
