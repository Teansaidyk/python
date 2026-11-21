sub, minutes = input("Подписка есть (да/нет): "), int(input("Длительность поездки, мин: "))
if sub == "да": print("Поездка входит в подписку" if minutes <= 30 else f"К оплате: {(minutes - 30) * 5} руб.")
else: print(f"К оплате: {50 + minutes * 8} руб.")
