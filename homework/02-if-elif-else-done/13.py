months, days = int(input("Отработано месяцев: ")), int(input("Дней отпуска: "))
if months < 6: print("Отпуск пока недоступен")
else:
    available = months * 28 // 12
    print(f"Доступно дней: {available}")
    print("Отпуск согласован" if days <= available else f"Не хватает дней: {days - available}")
