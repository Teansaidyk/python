n = int(input("Натуральное число: "))
div_sum = 0

for i in range(1, n):
    if n % i == 0:
        div_sum += i

if n > 0 and div_sum == n:
    print("Совершенное")
else:
    print("Не совершенное")
