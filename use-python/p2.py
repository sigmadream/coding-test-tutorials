from p0 import logging_time

INPUT_DATA = ["H", "e", "l", "l", "o"]


@logging_time
def reverse_string1(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s


print(reverse_string1(INPUT_DATA))


@logging_time
def reverse_string2(s: List[str]) -> str:
    # return s.reverse()
    s[:] = s[::-1]
    return s


print(reverse_string2(INPUT_DATA))
