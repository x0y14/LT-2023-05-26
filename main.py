from tokenizer import *

if __name__ == '__main__':
    j = """{"key":"value"}"""
    tokenizer = Tokenizer(j)
    tokens = tokenizer.tokenize()
    print(tokens)
