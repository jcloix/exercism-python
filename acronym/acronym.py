
def abbreviate(words):
    cleaned = words.replace("-", " ").replace("_", " ")
    acronym = [word[0].upper() for word in cleaned.split() if word]
    return "".join(acronym)
