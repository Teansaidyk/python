print ("1.1.9")
paint_price = 890
cans = 3
brush_price = 250
brushes = 2

paint_total = paint_price * cans
brush_total = brush_price * brushes
grand_total = paint_total + brush_total

print(f"Краска: {paint_total} руб.")
print(f"Кисти: {brush_total} руб.")
print(f"Всего: {grand_total} руб.")

print ("1.1.14")
balance = 5000  
balance = balance + 30000
print(f"После зарплаты: {balance}")
balance = balance - 18000
print(f"После аренды: {balance}")
balance = balance * 1.01
print(f"После кешбэка: {balance}")
balance = balance / 2
print(f"На карте осталось: {balance}")

print ("1.2.9")
kopecks = 12345
rubles = kopecks // 100
coins = kopecks % 100
print(f"{rubles} руб. {coins} коп.")

print ("1.2.12")
price_text = "250.5"
qty_text = "4"
total_cost = float(price_text) * int(qty_text)
print(f"Стоимость: {total_cost}")

print("1.3.8")
visitors = 120
orders = 18
conversion = (orders / visitors) * 100
print("Отчёт за день")
print(f"Посетителей: {visitors}")
print(f"Заказов: {orders}")
print(f"Конверсия: {conversion:.2f}%")

print("1.3.13")
product = "Ноутбук"
price = 54990
print(f"Товар: {product}")
print(f"Цена: {price} руб.")
print(f"С доставкой: {price + 500} руб.")

print("1.4.2")
a = 192
b = 168
c = 1
d = 10
print(f"{a}.{b}.{c}.{d}")

print("1.4.9")
dish = "Борщ"
price = 320
print(dish, end=" ... ")
print(f"{price} руб.")

print("1.5.7")
distance = 500
consumption = 7.5
price_per_liter = 55.9
fuel_needed = (distance / 100) * consumption
total_cost = fuel_needed * price_per_liter
print(f"Топлива: {fuel_needed:.2f} л")
print(f"Стоимость: {total_cost:.2f} руб.")

print("1.5.10")
base_fare = 99.0
price_per_km = 18.5
distance = 12.4
total_cost = base_fare + (price_per_km * distance)
print(f"Поездка: {total_cost:.2f} руб.")

print("1.5.14")
size_gb = 4.7
speed_mbps = 100.0
size_bits = size_gb * 1024 * 8
time_seconds = size_bits / speed_mbps
time_minutes = time_seconds / 60
print(f"Загрузка займёт {time_minutes:.2f} мин")

print("1.6.4")
x = 3
y = -2
print(f"Точка: ({x}, {y})")
print(f"Отражение: ({y}, {x})")

print("1.6.5")
a = 1
b = 2
c = 3
a, b, c = c, a, b
print(a, b, c)

print("1.6.14")
start_x = 2
start_y = 5
x = start_x
y = start_y
x, y = y, x + y
print(f"Одновременно: {x} {y}")
x = start_x
y = start_y
x = y
y = x + y
print(f"По очереди: {x} {y}")

print("1.6.15")
g1 = "Аня"
g2 = "Боря"
g3 = "Вика"
g4 = "Глеб"
g1, g2, g3, g4 = g2, g3, g4, g1
print(f"После тоста 1: {g1} {g2} {g3} {g4}")
g1, g2, g3, g4 = g2, g3, g4, g1
print(f"После тоста 2: {g1} {g2} {g3} {g4}")