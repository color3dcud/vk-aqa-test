def reverse_string(string: str) -> str:
    if string.lower() == string[::-1].lower():
        return 'This is palindrome!'
    else:
        return string[::-1]


a = reverse_string('kayak')
print(a)

b = reverse_string('hello')
print(b)
