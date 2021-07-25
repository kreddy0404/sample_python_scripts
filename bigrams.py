from nltk.tokenize import regexp_tokenize

tokens = []
bigrams = []

with open(input(), 'r', encoding='utf-8') as file:
    for line in file:
        tokens.extend(regexp_tokenize(line, "[^\\s]+"))

bigrams.extend([[tokens[i], tokens[i + 1]] for i in range(len(tokens)) if i != len(tokens) - 1])
print("Number of bigrams: ", len(bigrams))
print()

stop = False
while not stop:
    try:
        string = input()
        if string == "exit":
            stop = True
        elif string.isalpha():
            print(bigrams[string])
        else:
            integer = int(string)
            print("Head: {0} Tail: {1}".format(*bigrams[integer]))
    except TypeError:
        print("Type Error. Please input an integer.")
    except IndexError:
        print("Index Error. Please input an integer that is in the range of the corpus.")
