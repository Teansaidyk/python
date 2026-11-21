age = int(input("Возраст: "))

is_discount = age < 18 or age >= 65
print("Льготный билет:", is_discount)
print("Полный билет:", not is_discount)
