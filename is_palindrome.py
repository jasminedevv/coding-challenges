def is_palindrome(s):
    length = len(s)
    is_even = (length % 2 == 0)
    middle = length // 2
    if (is_even):
        left = s[:middle]
        right = s[middle:]
    else:
        left = s[:middle+1]
        right = s[middle:]
    if (left[::-1] == right):
        return True
    else:
        return False

assert is_palindrome('lool')
assert is_palindrome('lolol')
assert not is_palindrome('palindrome')