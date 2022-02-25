import collections
import re
from typing import List


paragraph = (
    "Bob hit a baU, bob, boB, a, a a a a a the hit BALL flew far after tt was hit."
)
banned = ["hit"]
# 데이터 정리


def mostCommonWord(paragraph: List[str], banned: List[str]) -> str:
    words = [
        word
        for word in re.sub(r"[^\w]", " ", paragraph).lower().split()
        if word not in banned
    ]

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]


print(mostCommonWord(paragraph, banned))
