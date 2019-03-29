from collections import Counter
from typing import List

with open("longtext.txt", 'r') as longtext:
    data: str = longtext.read()
words: List[str] = data.split()
counter: Counter = Counter(words)

print("Word counts:")
for letter, count in counter.items():
    print("{:13}: {:4}".format(letter, count))

print("250 most common:")
for letter, count in counter.most_common(250):
    print("{:8}: {:4}".format(letter, count))
