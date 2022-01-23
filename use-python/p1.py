"""
Q: 주어진 문자열이 팰린드롬인지 확인하라.
C1: 대소문자를 구분하지 않음
C2: 영문자와 숫자만 구분

입력:
- "A man, a plan, a canal: Panama"

출력
- true

입력:
- "race a car"

출력:
- false

"""


import collections
import re
from typing import Deque
from p0 import logging_time


@logging_time
def isPalindrome1(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


print(isPalindrome1("A man, a plan, a canal: Panama"))
print(isPalindrome1("race a car"))


@logging_time
def isPalindrome2(s: str) -> bool:

    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


print(isPalindrome2("A man, a plan, a canal: Panama"))
print(isPalindrome2("race a car"))


@logging_time
def isPalindrome3(s: str) -> bool:
    s = s.lower()
    s = re.sub("[^a-z0-9]", "", s)
    return s == s[::-1]


print(isPalindrome3("A man, a plan, a canal: Panama"))
print(isPalindrome3("race a car"))
