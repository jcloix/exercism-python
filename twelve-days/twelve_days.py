lyric_parts = [
    "a Partridge in a Pear Tree.",
    "two Turtle Doves, ",
    "three French Hens, ",
    "four Calling Birds, ",
    "five Gold Rings, ",
    "six Geese-a-Laying, ",
    "seven Swans-a-Swimming, ",
    "eight Maids-a-Milking, ",
    "nine Ladies Dancing, ",
    "ten Lords-a-Leaping, ",
    "eleven Pipers Piping, ",
    "twelve Drummers Drumming, ",
]
CONSTANT_VERSE = "On the {0} day of Christmas my true love gave to me: "
days = [
    "first",   
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
]
def recite(start_verse, end_verse):
    result = []
    for day in range(start_verse, end_verse + 1):
        verse = CONSTANT_VERSE.format(days[day - 1])
        for part in range(day, 0, -1):
            if day > 1 and part == 1:
                verse += "and "
            verse += lyric_parts[part - 1]
        result.append(verse)
    return result
