n = int(input("Номер заказа: "))
total = 0
while n > 0:
    total += n % 10
    n //= 10
print("Сумма цифр:", total)
