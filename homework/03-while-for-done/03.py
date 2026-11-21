n = int(input("Натуральное число: "))
count = 0
while n > 0:
    count += 1
    n //= 10
print("Цифр:", count)
