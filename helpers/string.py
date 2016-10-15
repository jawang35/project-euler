def palindrome(string):
    if (len(string) < 2):
        return True
    if (not string.endswith(string[0])):
        return False
    return palindrome(string[1:-1])
