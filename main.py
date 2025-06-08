import tiktoken

def main():
    with open("input/quijote.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()
        
    print("Total number of character:", len(raw_text))
    
    text = ("hola como estamos mi gente") 

    tokenizer = tiktoken.get_encoding("gpt2")
    integers = tokenizer.encode(text)

    print(tokenizer.decode(integers))

if __name__ == "__main__":
    main()
