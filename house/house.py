parts = [
    ("house", "that Jack built"),
    ("malt", "that lay in the house"),
    ("rat", "that ate the malt"),
    ("cat", "that killed the rat"),
    ("dog", "that worried the cat"),
    ("cow with the crumpled horn", "that tossed the dog"),
    ("maiden all forlorn", "that milked the cow with the crumpled horn"),
    ("man all tattered and torn", "that kissed the maiden all forlorn"),
    ("priest all shaven and shorn", "that married the man all tattered and torn"),
    ("rooster that crowed in the morn", "that woke the priest all shaven and shorn"),
    ("farmer sowing his corn", "that kept the rooster that crowed in the morn"),
    ("horse and the hound and the horn", "that belonged to the farmer sowing his corn"),
]

def recite(start_verse, end_verse):
    result = []
    for verse in range(start_verse, end_verse + 1):
        lines = ["This is the " + parts[verse - 1][0]]
        for i in range(verse - 1, -1, -1):
            lines.append(parts[i][1])
        result.append(" ".join(lines) + ".")
    return result