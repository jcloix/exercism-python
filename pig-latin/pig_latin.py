def translate(text):
    result = ""
    for word in text.split():
        result += translateWord(word) + " "
    return result.strip()

def translateWord(text):
    vowelIndex = firstVowelIndex(text)
    if vowelIndex == 0 or text[:2] in ["xr", "yt"]:
        return text + "ay"
    if "y" in text[1:]:
            y_index = text.index("y")
            if all(c not in "aeiou" for c in text[:y_index]):
                return text[y_index:] + text[:y_index] + "ay"

    if "qu" in text:
        qu_index = text.index("qu") + 2
        if all(c not in "aeiou" for c in text[:qu_index - 2]):
            return text[qu_index:] + text[:qu_index] + "ay"

    if vowelIndex > 0:
        return text[vowelIndex:] + text[:vowelIndex] + "ay"

    return text

def firstVowelIndex(text):
    return next((i for i, c in enumerate(text) if c in "aeiou"), -1)