from collections import defaultdict, Counter
import random
words = []
with open(input(), "r", encoding="utf-8") as file:
    for line in file:
        words.extend(line.split())
bigrams = list(zip(words, words[1:]))
bigrams_dict = defaultdict(Counter)
for h, t in bigrams:
    bigrams_dict[h][t] += 1
print(list(bigrams_dict[random.choice(words)].values()))
