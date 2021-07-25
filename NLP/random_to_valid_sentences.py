from collections import defaultdict, Counter
from nltk import WhitespaceTokenizer, bigrams
from random import choice, choices

bigrams_list = []
bigrams_dict = defaultdict(Counter)

with open(input(), 'r', encoding='utf-8') as file:
    for line in file:
        bigrams_list.extend(bigrams(WhitespaceTokenizer().tokenize(line)))

for head, tail in bigrams_list:
    bigrams_dict[head][tail] += 1

heads = list(bigrams_dict.keys())

first_word_set = set()
while len(first_word_set) < 10:
    word = choice(heads)
    if word[0].isupper() and word[-1] not in ".!?":
        first_word_set.add(word)

for word in first_word_set:
    sentence = [word]
    while len(sentence) < 5 or sentence[-1][-1] not in ".!?":
        next_words = list(bigrams_dict[sentence[-1]].keys())
        next_words_count = list(bigrams_dict[sentence[-1]].values())
        sentence.extend(choices(next_words, weights=next_words_count))
    print(" ".join(sentence))
