charge = int(input("Заряд, %: "))

if charge == 100:
    print("Батарея заряжена")
elif charge <= 20:
    print("Критический заряд")
elif charge <= 50:
    print("Низкий заряд")
else:
    print("Нормальный заряд")
