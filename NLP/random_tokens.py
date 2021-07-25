from collections import defaultdict, Counter
from nltk import WhitespaceTokenizer, bigrams
from random import choice, choices

bigrams_list = []
bigrams_dict = defaultdict(list)

with open(input(), 'r', encoding='utf-8') as file:
    for line in file:
        bigrams_list.extend(bigrams(WhitespaceTokenizer().tokenize(line)))

for head, tail in bigrams_list:
    bigrams_dict[head].append(tail)

bigrams_dict = {head: dict(Counter(tail)) for head, tail in bigrams_dict.items()}

for _ in range(10):
    first_word = choice(list(bigrams_dict.keys()))
    other_words = choices(list(bigrams_dict[first_word].keys()), weights=list(bigrams_dict[first_word].values()), k=10)
    print(first_word + " ".join(other_words))
