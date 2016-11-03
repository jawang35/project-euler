def is_palindrome(string):
    if (len(string) < 2):
        return True
    if (not string.endswith(string[0])):
        return False
    return is_palindrome(string[1:-1])
