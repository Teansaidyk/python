pin_code = 4821
attempts = 0

while attempts < 3:
    guess = int(input("PIN-код: "))
    attempts += 1
    if guess == pin_code:
        print("Доступ разрешён")
        break
else:
    print("Карта заблокирована")
