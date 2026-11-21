total = 0
count = 0
num = int(input("Число (0 — конец): "))

while num != 0:
    total += num
    count += 1
    num = int(input("Число (0 — конец): "))

print("Сумма:", total)
print("Количество:", count)
