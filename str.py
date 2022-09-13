def reverse_string(string: str) -> str:
    if string.lower() == string[::-1].lower():
        return 'This is palindrome!'
    else:
        return string[::-1]
