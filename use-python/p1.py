import collections
import re
from p0 import logging_time

INPUT_DATA1 = "A man, a plan, a canal: Panama"
INPUT_DATA2 = "race a car"


@logging_time
def is_palindrome1(s):
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


print(is_palindrome1(INPUT_DATA1))
print(is_palindrome1(INPUT_DATA2))


@logging_time
def is_palindrome2(s: str) -> bool:
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


print(is_palindrome2(INPUT_DATA1))
print(is_palindrome2(INPUT_DATA2))


@logging_time
def is_palindrome3(s: str) -> bool:
    s = s.lower()
    s = re.sub("[^a-z0-9]", "", s)
    return s == s[::-1]


print(is_palindrome3(INPUT_DATA1))
print(is_palindrome3(INPUT_DATA2))
