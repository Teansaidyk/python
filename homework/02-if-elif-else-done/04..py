start, end, actual = int(input("Начало: ")), int(input("Конец: ")), int(input("Факт: "))
if actual < start: print("Раньше интервала")
elif actual <= end: print("Вовремя")
else: print(f"Опоздание на {actual - end} ч")
