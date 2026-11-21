n = int(input("Число показаний: "))
total = 0

for i in range(n):
    val = int(input("Показание, °C: "))
    total += val
    if i == 0 or val < min_val:
        min_val = val

print("Минимум:", min_val)
print(f"Среднее: {total / n:.2f}")
