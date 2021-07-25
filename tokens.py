from nltk.tokenize import regexp_tokenize

tokens = []
unique_tokens = []

with open(input(), 'r', encoding='utf-8') as file:
    for line in file:
        tokens.extend(regexp_tokenize(line, "[^\\s]+"))

print("Corpus statistics")
print("All tokens: ", len(tokens))
print("Unique tokens: ", len(set(tokens)))
print()

stop = False
while not stop:
    try:
        string = input()
        if string == "exit":
            stop = True
        elif string.isalpha():
            print(tokens[string])
        else:
            print(tokens[int(string)])
    except TypeError:
        print("Type Error. Please input an integer.")
    except IndexError:
        print("Index Error. Please input an integer that is in the range of the corpus.")
