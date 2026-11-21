pressure = float(input("Давление, бар: "))

if pressure < 2.0:
    print("Подкачайте шины")
elif pressure <= 2.5:
    print("Давление в норме")
else:
    print("Снизьте давление")
    