height = int(input("Рост, см: "))
age = int(input("Возраст: "))
adult = input("Со взрослым (да/нет): ") == "да"

can_ride = height >= 130 or (height >= 120 and age >= 8 and adult)
print("Можно на аттракцион:", can_ride)
