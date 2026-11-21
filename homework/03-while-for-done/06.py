total = 0
count = 0
grade = int(input("Оценка (0 — конец): "))

while grade != 0:
    total += grade
    count += 1
    grade = int(input("Оценка (0 — конец): "))

if count == 0:
    print("Оценок нет")
else:
    print(f"Средний балл: {total / count:.2f}")
