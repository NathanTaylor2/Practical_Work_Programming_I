def main():
    import random

    VOWELS = "aeiou"
    CONSONANTS = "bcdfghjklmnpqrstvwxyz"
    ALL = "aeioubcdfghjklmnpqrstvwxyz"

    word_format = input("Input here")
    word = ""
    for kind in word_format:
        if kind == "%":
            word += random.choice(CONSONANTS)
        elif kind == "#":
            word += random.choice(VOWELS)
        elif kind == "*":
            word += random.choice(ALL)
        else:
            word += kind
    print(word)

main()