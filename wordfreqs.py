from collections import Counter
from typing import List

words: List[str] = open("longtext.txt", 'r').read().split()
counter: Counter = Counter(words)

# print("Word counts:")
# for letter, count in counter.items():
#     print("{:13}: {:4}".format(letter, count))

print("250 most common words:")
for word, count in counter.most_common(250):
    print("{:8}: {:4}".format(word, count))
