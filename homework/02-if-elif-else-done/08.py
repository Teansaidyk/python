limit = int(input("Разрешённая скорость, км/ч: "))
speed = int(input("Фактическая скорость, км/ч: "))
over = speed - limit

if over <= 20:
    fine = 0
elif over <= 40:
    fine = 750
elif over <= 60:
    fine = 1500
elif over <= 80:
    fine = 2500
else:
    fine = 5000

print(f"Штраф: {fine} руб.")
