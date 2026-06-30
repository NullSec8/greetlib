def greet(name: str, greeting: str = "Hello") -> str:
    """Return a friendly greeting."""
    return f"{greeting}, {name}!"

def greet_many(names: list[str], greeting: str = "Hello") -> list[str]:
    """Greet multiple people."""
    return [greet(name, greeting) for name in names]
