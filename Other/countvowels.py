word = input("enter a word: ")
vowel = 0
count = 0

while count < len(word):
    x = word[count]
    if x.lower() in "aeiou":
        vowel += 1
    count += 1 

print(f"number of vowels in '{word}' is {vowel}")
