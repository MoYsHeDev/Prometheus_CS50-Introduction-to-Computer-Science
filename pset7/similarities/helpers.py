from nltk.tokenize import sent_tokenize


def lines(a: str, b: str) -> set & set:
    """Return lines in both a and b"""

    a_lines = set(a.splitlines())
    b_lines = set(b.splitlines())

    return a_lines and b_lines
    

def sentences(a: str, b: str) -> set & set:
    """Return sentences in both a and b"""

    a_sentences = set(sent_tokenize(a))
    b_sentences = set(sent_tokenize(b))

    return a_sentences and b_sentences


def substrings(a: str, b: str, n: int) -> set & set:
    """Return substrings of length n in both a and b"""

    def substring_tokenizer(string: str, length: int) -> list:
        """Return substrings of length "length" in both "string" """
        substrings_str = []

        for i in range(0, len(string) - length):
            temp = string[i:i + length]
            substrings_str.append(temp)

        return substrings_str

    a_substrings = set(substring_tokenizer(a, n))
    b_substrings = set(substring_tokenizer(b, n))

    return a_substrings and b_substrings
