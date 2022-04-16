import collections
import re

from p0 import logging_time

input_paragraph = (
    "Bob hit a baU, bob, boB, a, a a a a a the hit BALL flew far after tt was hit."
)
input_banned = ["hit"]


@logging_time
def most_common_word(paragraph, banned):
    words = [
        word
        for word in re.sub(r"[^\w]", " ", paragraph).lower().split()
        if word not in banned
    ]

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]


print(most_common_word(input_paragraph, input_banned))
