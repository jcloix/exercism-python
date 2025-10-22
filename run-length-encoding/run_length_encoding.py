import re
def decode(string):
    pattern = r'(\d+)([a-zA-Z ])|.'
    return ''.join(
        m.group(2) * int(m.group(1))
        if m.group(1) else m.group(0)
        for m in re.finditer(pattern, string)
    )

def encode(string):
    pattern = r'([a-zA-Z ])\1*'
    return ''.join(
        f"{len(m.group(0))}{m.group(1)}"
        if m.group(1) and len(m.group(0)) > 1
        else m.group(0)
        for m in re.finditer(pattern, string)
    )
