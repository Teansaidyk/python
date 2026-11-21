secret = 37
attempt = 0

while attempt < 5:
    attempt += 1
    guess = int(input("Ваша догадка: "))
    if guess == secret:
        print("Угадано с попытки", attempt)
        break
    elif guess > secret:
        print("Меньше")
    else:
        print("Больше")
else:
    print("Попытки закончились")
