from enum import Enum


class TokenKind(Enum):
    EOF = 1      # end of file

    STRING = 2   # "string"
    NUMERIC = 3  # 123

    LSB = 4      # [
    RSB = 5      # ]
    LCB = 6      # {
    RCB = 7      # }

    COLON = 8    # :
    SEMI = 9     # ;

    ADD = 10     # +
    SUB = 11     # -


class Token:
    def __init__(self, kind, value=""):
        self.kind = kind
        self.value = value


# 文字列を規則に従って切り分ける
class Tokenizer:
    def __init__(self, json):
        self.input = json
        self.pos = 0
        self.tokens = []

    def is_eof(self):
        return len(self.input) <= self.pos

    def current(self):
        return self.input[self.pos]

    def is_symbol(self):
        return self.current() in ["{", "}", ":"]

    def is_alpha(self):
        return self.current().isalpha()

    def is_numeric(self):
        return self.current().isnumeric()

    def consume_symbol(self):
        symbol = self.current()
        self.pos += 1
        return symbol

    def consume_string(self):
        assert self.current() == "\""
        self.pos += 1
        s = ""
        while self.is_alpha():
            s += self.current()
            self.pos += 1

        assert self.current() == "\""
        self.pos += 1
        return s

    def consume_numeric(self):
        s = ""
        while self.is_numeric():
            s += self.current()
            self.pos += 1
        return int(s)

    def tokenize(self):
        while not self.is_eof():
            if self.is_symbol():
                self.tokens.append(self.consume_symbol())
            elif self.current() == "\"":
                self.tokens.append(self.consume_string())
            elif self.is_numeric():
                self.tokens.append(self.consume_numeric())

        return self.tokens

