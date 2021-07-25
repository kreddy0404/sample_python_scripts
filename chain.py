from nltk.tokenize import regexp_tokenize
from collections import defaultdict, Counter

tokens = []
bigrams = []

with open(input(), 'r', encoding='utf-8') as file:
    for line in file:
        tokens.extend(regexp_tokenize(line, "[^\\s]+"))

bigrams.extend([[tokens[i], tokens[i + 1]] for i in range(len(tokens)) if i != len(tokens) - 1])

bigrams_dict = defaultdict(list)

for head, tail in bigrams:
    bigrams_dict[head].append(tail)

bigrams_dict = {head: dict(Counter(tail)) for head, tail in bigrams_dict.items()}


while (head := input()) != 'exit':
    try:
        print(f"Head: {head}")
        print("\n".join(f'Tail: {k} Count: {v}' for k, v in bigrams_dict[head].items()))
    except KeyError:
        print("Key Error. The requested word is not in the model. Please input another word.")
