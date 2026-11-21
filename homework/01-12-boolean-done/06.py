age = int(input("Возраст: "))
exp = input("Опыт работы есть (да/нет): ") == "да"

print("Подходит:", 18 <= age <= 65 and exp)
