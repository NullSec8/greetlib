import argparse
import random
from greetlib import greet, greet_random, print_banner, LANGUAGES, STYLES, COLORS


def main():
    parser = argparse.ArgumentParser(
        description="Greet people in style!",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("name", help="Who to greet")
    parser.add_argument("-s", "--style", choices=list(STYLES.keys()), default="normal",
                        help=f"Greeting style (default: normal)")
    parser.add_argument("-l", "--lang", choices=list(LANGUAGES.keys()), default="english",
                        help=f"Language (default: english)")
    parser.add_argument("-c", "--color", choices=[k for k in COLORS if k != "reset"],
                        help="Text color")
    parser.add_argument("--random", action="store_true",
                        help="Random style, language, and color")
    parser.add_argument("--banner", action="store_true",
                        help="Show banner before greeting")

    args = parser.parse_args()

    if args.banner:
        print_banner()

    if args.random:
        msg = greet_random(args.name)
    else:
        msg = greet(args.name, args.style, args.lang, args.color)

    print(msg)


if __name__ == "__main__":
    main()
