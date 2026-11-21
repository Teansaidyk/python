n = int(input("Число покупок: "))
total = 0
for _ in range(n):
    total += int(input("Цена покупки, руб.: "))
print(f"Итого: {total} руб.")
