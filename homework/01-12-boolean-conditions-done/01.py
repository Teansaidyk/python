stock = int(input("Остаток на складе, шт.: "))
price = int(input("Цена товара, руб.: "))
money = int(input("Деньги у покупателя, руб.: "))

print(stock > 0 and money >= price)
