import random

STYLES = {
    "normal": "Hello",
    "formal": "Greetings",
    "casual": "Yo",
    "pirate": "Ahoy",
    "alien": "👽 Blork",
    "robot": "01001000 01100101 01101100 01101100 01101111",
    "doge": "Such greet, very",
    "shouty": "HELLO",
}

LANGUAGES = {
    "english": "Hello",
    "spanish": "Hola",
    "french": "Bonjour",
    "german": "Hallo",
    "italian": "Ciao",
    "japanese": "こんにちは",
    "arabic": "مرحبا",
    "hindi": "नमस्ते",
    "russian": "Привет",
    "korean": "안녕하세요",
}

COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "reset": "\033[0m",
}

BANNER = """
  ╔══════════════════════════════════╗
  ║     🌟  GREETLIB  🌟            ║
  ║  Say it in style!               ║
  ╚══════════════════════════════════╝
"""


def greet(name, style="normal", lang="english", color=None):
    greeting = STYLES.get(style, STYLES["normal"])
    if lang in LANGUAGES:
        greeting = LANGUAGES[lang]
    msg = f"{greeting}, {name}!"
    if color and color in COLORS:
        msg = f"{COLORS[color]}{msg}{COLORS['reset']}"
    return msg


def greet_random(name):
    style = random.choice(list(STYLES.keys()))
    lang = random.choice(list(LANGUAGES.keys()))
    color = random.choice(list(COLORS.keys()))
    return greet(name, style, lang, color)


def greet_many(names, style="normal", lang="english"):
    return [greet(n, style, lang) for n in names]


def get_random_greeting():
    return random.choice(list(LANGUAGES.values()))


def print_banner():
    print(f"{COLORS['cyan']}{BANNER}{COLORS['reset']}")
