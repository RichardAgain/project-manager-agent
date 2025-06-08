import re

class SimpleTokenizerV1:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for s,i in vocab.items()}
    
    def encode(self, text: str):
        preprocessed = re.split(r'([-,.:;¿?_¡!«»"()\']|--|\s)', text)
        preprocessed = [item for item in preprocessed if item]
        
        ids = [self.str_to_int[i] for i in preprocessed]
        return ids
        
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text

def build_vocab(text: str):
    preprocessed = re.split(r'([-,.:;¿?_¡!«»"()\']|--|\s)', text)
    preprocessed = [item for item in preprocessed if item]
    
    all_words = sorted(set(preprocessed))
    
    vocab = {token: integer for integer, token in enumerate(all_words)}
    
    return vocab