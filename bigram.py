import random
from collections import defaultdict
from utils.tokenizer import SimpleTokenizerV1, build_vocab

with open("input/quijote.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

vocab = build_vocab(raw_text)
tokenizer = SimpleTokenizerV1(vocab)

bigram_model = defaultdict(lambda: defaultdict(lambda: 0))

text = tokenizer.encode(raw_text)

for i in range(1, len(text)):
    bigram_model[text[i-1]][text[i]] += 1 

def predict_word(token):
    next_word = bigram_model[token]
    
    words = list(next_word.keys())
    weights = list(next_word.values())

    predicted_word = random.choices(words, weights)[0]
    
    return predicted_word     

    # if next_word:
    #     print(next_word)
    #     predicted_word = max(next_word, key=next_word.get)
    #     return predicted_word
    # else:
    #     return None

def predict_next_n_words(input, n=100):
    encoded = tokenizer.encode(input)

    result = [encoded[-1]]
    for _ in range(n):
        next_token = predict_word(result[-1])
        result.append(next_token)
    return tokenizer.decode(result)
