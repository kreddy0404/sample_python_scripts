from collections import defaultdict, Counter
from nltk import WhitespaceTokenizer
from random import choice, choices


tokens = []
trigrams = []
trigrams_dict = defaultdict(Counter)

with open(input(), 'r', encoding='utf-8') as file:
    for line in file:
        tokens.extend(WhitespaceTokenizer().tokenize(line))

trigrams = list(zip(tokens, tokens[1:], tokens[2:]))

for h1, h2, t in trigrams:
    trigrams_dict[h1 + " " + h2][t] += 1

heads = list(trigrams_dict.keys())

first_word_set = set()
while len(first_word_set) < 10:
    word = choice(heads)
    if word[0].isupper() and word.split()[0][-1] not in ".!?" and word[-1] not in ".!?":
        first_word_set.add(word)

for word in first_word_set:
    sentence = [word]
    while len(sentence) < 4 or sentence[-1][-1] not in ".!?":
        if len(sentence) <= 1:
            next_head = sentence[-1]
        elif len(sentence) == 2:
            next_head = " ".join([sentence[-2].split()[1], sentence[-1]])
        else:
            next_head = " ".join(sentence[-2::])

        next_items = trigrams_dict.get(next_head).most_common()
        next_words = [w[0] for w in next_items]
        next_words_count = [c[1] for c in next_items]
        sentence.extend(choices(next_words, weights=next_words_count))
    print(" ".join(sentence))
