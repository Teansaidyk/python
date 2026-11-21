text = input("Фраза: ")
words = 0
in_word = False

for ch in text:
    if ch != " " and not in_word:
        words += 1
        in_word = True
    elif ch == " ":
        in_word = False

print("Слов:", words)
