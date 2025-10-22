def is_pangram(sentence):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    sentence_set = set(sentence.lower())
    if alphabet.issubset(sentence_set):
        return True
    return False
