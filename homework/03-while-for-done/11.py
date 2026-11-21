prices = [150, 450, 990, 80, 320, 200]

limit = int(input("Порог цены, руб.: "))
count = 0
for price in prices:
    if price > limit:
        count += 1
print("Дороже порога:", count)
