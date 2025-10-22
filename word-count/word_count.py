

import re
def count_words(sentence):
    # Replace underscores with spaces to split words like "my_spacebar_is_broken"
    sentence = sentence.replace("_", " ")
    # Find words, allowing apostrophes only within words (not at the start or end)
    words = re.findall(r"\b[a-zA-Z0-9]+(?:'[a-zA-Z0-9]+)?\b", sentence.lower())
    return {word: words.count(word) for word in set(words)}