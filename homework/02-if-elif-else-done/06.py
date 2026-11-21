category = input("Категория: ")
amount = float(input("Сумма покупки, руб.: "))

if category == "азс":
    percent = 0.05
elif category == "аптека":
    percent = 0.03
elif category == "супермаркет":
    percent = 0.01
else:
    percent = 0.0

cashback = amount * percent
print(f"Кешбэк: {cashback:.2f} руб.")
