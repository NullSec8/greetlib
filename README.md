# greetlib 🌟

**Greet people in style** — colors, languages, pirate mode, ASCII banners, and more!

## Install

```bash
pip install --extra-index-url https://pypi.pkg.github.com/NullSec8/simple/ greetlib
```

## CLI Usage

```bash
# Basic
greetlib Alice

# Different styles
greetlib Bob --style pirate
greetlib Charlie --style doge
greetlib Dave --style shouty

# Languages
greetlib Eve --lang spanish
greetlib Frank --lang japanese
greetlib Grace --lang hindi

# With color + banner
greetlib Hank --color magenta --banner

# Random mode (random style + language + color)
greetlib Ivy --random
```

### Styles

| Style | Output |
|-------|--------|
| normal | Hello, World! |
| formal | Greetings, World! |
| casual | Yo, World! |
| pirate | Ahoy, World! |
| alien | 👽 Blork, World! |
| robot | 01001000 01100101 01101100 01101100 01101111, World! |
| doge | Such greet, very, World! |
| shouty | HELLO, World! |

### Languages

english, spanish, french, german, italian, japanese, arabic, hindi, russian, korean

## Python Usage

```python
from greetlib import greet, greet_random, greet_many, print_banner

print_banner()
print(greet("Alice", style="pirate", color="red"))
print(greet("Bob", lang="spanish"))
print(greet_random("Charlie"))
print(greet_many(["X", "Y", "Z"], style="doge"))
```

## How it works

GitHub Actions builds the package and publishes it to **GitHub Packages** on every tag push. Then `pip` can install it directly from there.
