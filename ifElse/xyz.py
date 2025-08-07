s = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
words = s.split()  # Split sentence into words

for word in words:
    has_vowel = False
    for char in word:
        if char in vowels:
            has_vowel = True
            break
    if has_vowel:
        print(f"'{word}' has a vowel.")
    else:
        print(f"'{word}' has no vowels.")
