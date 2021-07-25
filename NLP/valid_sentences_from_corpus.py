from nltk import sent_tokenize


def load_text(file_name_):
    with open(file_name_, encoding='utf-8') as file_:
        return file_.read()


text = load_text(input())
sentences = sent_tokenize(text)
sentences_to_print = []
for sentence in sentences:
    tokens = sentence.split()
    if len(tokens) >= 5 and not tokens[0].endswith(('.', '!', '?')) and tokens[-1].endswith(('.', '!', '?')):
        sentence.capitalize()
        if len(sentences_to_print) < 10:
            sentences_to_print.extend([sentence])
        else:
            break

print("\n".join(sentences_to_print))
