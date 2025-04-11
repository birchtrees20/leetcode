import string

def is_palindrome(s: str) -> bool:
    # Remove spaces and punctuation, and convert to lowercase
    cleaned_s = ''.join(c.lower() for c in s if c.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned_s == cleaned_s[::-1]
