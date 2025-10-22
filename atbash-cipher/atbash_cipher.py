import string
atbash_table = str.maketrans(
    string.ascii_lowercase + string.ascii_uppercase,
    string.ascii_lowercase[::-1] + string.ascii_lowercase[::-1]
)

def encode(plain_text):
    plain_text = plain_text.translate(atbash_table)
    plain_text = ''.join(filter(str.isalnum, plain_text)).lower()
    # Add spaces every 5 characters
    return ' '.join(plain_text[i:i+5] for i in range(0, len(plain_text), 5))


def decode(ciphered_text):
    ciphered_text = ciphered_text.replace(" ", "")
    return ciphered_text.translate(atbash_table)
