# python_v2/my_library/string_utils.py

def reverse_string(s: str) -> str:
    """Reverses a given string."""
    return s[::-1]

def capitalize_string(s: str) -> str:
    """Capitalizes the first letter of a string."""
    if not s:
        return ""
    return s.capitalize()

def is_palindrome(s: str) -> bool:
    """Checks if a string is a palindrome (reads the same forwards and backwards)."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]