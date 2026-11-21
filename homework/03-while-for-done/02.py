total = 0
steps = int(input("Шаги за день (0 — конец): "))
while steps != 0:
    total += steps
    steps = int(input("Шаги за день (0 — конец): "))
print("Всего шагов:", total)
