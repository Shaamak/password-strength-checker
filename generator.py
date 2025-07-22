import itertools

leet_map = {
    'a': ['a', '@', '4'],
    'e': ['e', '3'],
    'i': ['i', '1', '!'],
    'o': ['o', '0'],
    's': ['s', '$', '5'],
    't': ['t', '7']
}

years = ['2024', '2023', '123', '007']

def leetspeak_variants(word):
    options = []
    for char in word.lower():
        if char in leet_map:
            options.append(leet_map[char])
        else:
            options.append([char])
    return set(''.join(i) for i in itertools.product(*options))

def generate_wordlist(inputs):
    wordlist = set()

    for word in inputs:
        variants = leetspeak_variants(word)
        for variant in variants:
            wordlist.add(variant)
            for y in years:
                wordlist.add(variant + y)
                wordlist.add(y + variant)

    return sorted(wordlist)
