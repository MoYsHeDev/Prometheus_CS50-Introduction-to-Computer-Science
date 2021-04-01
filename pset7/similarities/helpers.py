from nltk.tokenize import sent_tokenize


def lines(a: str, b: str):
    """Return lines in both a and b"""

    a_lines = set(a.splitlines())
    b_lines = set(b.splitlines())

    return a_lines & b_lines
    

def sentences(a: str, b: str):
    """Return sentences in both a and b"""

    a_sentences = set(sent_tokenize(a))
    b_sentences = set(sent_tokenize(b))

    return a_sentences & b_sentences


def substring_tokenizer(string: str, length: int) -> str:
    """Return substrings of length "length" in both "string" """
    substrings_str = []

    for i in range(len(string) - length + 1):
        substrings_str.append(string[i:i + length])
    return substrings_str


def substrings(a: str, b: str, n: int):
    """Return substrings of length n in both a and b"""

    a_substrings = set(substring_tokenizer(a, n))
    b_substrings = set(substring_tokenizer(b, n))

    return a_substrings & b_substrings