def find_anagrams(word, candidates):
    cleaned = word.lower()
    result = [c for c in candidates if c.lower() != cleaned and sorted(c.lower()) == sorted(cleaned)]
    return result
