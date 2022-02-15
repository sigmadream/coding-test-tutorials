"""
Q: 문자열을 뒤집는 함수를 작성하라. 
C1: 입력값은 배열
C2: 리턴없이 리스트 내부를 직접 조작

입력:
["h", "e", "l", "l", "o"]

출력:
["o", "l", "l", "e", "H"]
"""
from typing import List

from p0 import logging_time


@logging_time
def reverse_string1(s: List[str]) -> str:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s


print(reverse_string1(["H", "e", "l", "l", "o"]))


@logging_time
def reverse_string2(s: List[str]) -> str:
    # return s.reverse()
    s[:] = s[::-1]
    return s


print(reverse_string2(["H", "e", "l", "l", "o"]))
