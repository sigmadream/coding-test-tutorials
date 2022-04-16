from p0 import logging_time

INPUT_DATA1 = "babad"
INPUT_DATA2 = "cbbd"


@logging_time
def longest_palindrome(s):
    def expand(left, right):
        while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
            left -= 1
            right += 1
        return s[left + 1:right - 1]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''

    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

    return result


print(longest_palindrome(INPUT_DATA1))
print(longest_palindrome(INPUT_DATA2))
