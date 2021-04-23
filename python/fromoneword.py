def ana(first_word, second_word):
    for char in second_word:
        if char not in first_word:
            return "no"
    return "yes"

first_word, second_word = map(str, input().split())

print(ana(first_word, second_word))
