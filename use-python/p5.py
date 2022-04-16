import collections
from p0 import logging_time

INPUT_DATA = ["eat", "tea", "tan", "ate", "nat", "bat"]


@logging_time
def group_anagrams(strs):
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return anagrams.values()


print(group_anagrams(INPUT_DATA))
