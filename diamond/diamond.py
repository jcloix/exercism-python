def rows(letter):
    if letter < 'A' or letter > 'Z':
        raise ValueError("Input must be an uppercase letter from A to Z")
    diamond = []
    size = ord(letter) - ord('A')
    for i in range(size + 1):
        line = ' ' * (size - i)
        line += chr(ord('A') + i)
        if i > 0:
            line += ' ' * (i * 2 - 1) + chr(ord('A') + i)
        line += ' ' * (size - i)    
        diamond.append(line)
    diamond += diamond[-2::-1]
    return diamond
