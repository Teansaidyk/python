on_time, score = input("Сдана в срок (да/нет): "), int(input("Баллы: "))
if not (0 <= score <= 10): print("Ошибка ввода")
elif score < 5: print("Работа не зачтена")
else:
    if on_time == "да": print(f"Оценка: {5 if score >= 9 else 4 if score >= 7 else 3}")
    else: print("Оценка: 3")
