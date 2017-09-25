import string

RULES = {
    'a': ['@', '4'], # a becomes @ or 4
    'A': ['@', '4'],
    'b': ['8'],
    'B': ['8'],
    'e': ['3'],
    'E': ['3'],
    'i': ['!', '1'],
    'I': ['!', '1'],
    'o': ['0'],
    'O': ['0'],
    's': ['$'],
    'S': ['$'],
    't': ['+', '7'],
    'T': ['+', '7']
}

def add_rules_lower_to_upper():
    for lower_char in string.ascii_lowercase:
        upper_char = lower_char.upper()
        try:
            RULES[lower_char].append(upper_char)
        except KeyError:
            RULES[lower_char] = [upper_char]

def add_rules_upper_to_lower():
    for upper_char in string.ascii_uppercase:
        lower_char = upper_char.lower()
        try:
            RULES[upper_char].append(lower_char)
        except KeyError:
            RULES[upper_char] = [lower_char]
