"""Consume greetlib from GitHub Packages."""

from greetlib import greet, greet_random, greet_many, print_banner, LANGUAGES

print_banner()
print(greet("Alice", style="pirate", color="red"))
print(greet("Bob", lang="spanish"))
print(greet("Charlie", style="doge", color="yellow"))
print(greet_random("Diana"))
print()

print("All languages:")
for lang in LANGUAGES:
    print(f"  {greet('World', lang=lang)}")
