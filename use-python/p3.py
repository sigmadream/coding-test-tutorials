from p0 import logging_time

INPUT_DATA1 = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
INPUT_DATA2 = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]

@logging_time
def reorder_log_files(logs):
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits


answer1 = reorder_log_files(INPUT_DATA1)
answer2 = reorder_log_files(INPUT_DATA2)
