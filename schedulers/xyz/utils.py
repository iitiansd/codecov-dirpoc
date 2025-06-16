# schedulers/xyz/utils.py
def greet(name: str) -> str:
    if not name:
        raise ValueError("Name must not be empty")
    return f"Hello, {name}!"
