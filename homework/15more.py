print("1.1.10")
monday = 450
tuesday = 300
wednesday = 600
total = monday + tuesday + wednesday
average = total / 3
print(f"Всего: {total} руб.")
print(f"В среднем за день: {average} руб.")

print("1.1.11")
price = 36000
months = 12
monthly_payment = price / months
paid_5_months = monthly_payment * 5
remaining = price - paid_5_months
print(f"Платёж в месяц: {monthly_payment}")
print(f"Выплачено за 5 месяцев: {paid_5_months}")
print(f"Осталось: {remaining}")

print("1.1.12")
subscription = 450
extra_gb = 3
gb_price = 120
sms = 10
sms_price = 2.5
internet_total = extra_gb * gb_price
sms_total = sms * sms_price
grand_total = subscription + internet_total + sms_total
print(f"Абонентская плата: {subscription}")
print(f"Доп. интернет: {internet_total}")
print(f"SMS: {sms_total}")
print(f"Итого: {grand_total}")

print("1.2.4")
eggs = 100
per_box = 12
boxes = eggs // per_box
leftover = eggs % per_box
print(f"Полных коробок: {boxes}")
print(f"Осталось яиц: {leftover}")

print("1.2.8")
day1_text = "25"
day2_text = "17"
concatenated = day1_text + day2_text
real_sum = int(day1_text) + int(day2_text)
print(f"Склеились: {concatenated}")
print(f"Сумма: {real_sum}")

print("1.2.15")
now_hours = 10
now_minutes = 14
end_total_minutes = 11 * 60 + 30
now_total_minutes = now_hours * 60 + now_minutes
remaining_minutes = end_total_minutes - now_total_minutes
left_hours = remaining_minutes // 60
left_minutes = remaining_minutes % 60
print(f"До конца пары: {left_hours} ч {left_minutes} мин")

print("1.3.5")
rubles = 10000
rate = 92.35
dollars = rubles / rate
print(f"{rubles} руб. = {dollars:.2f} $")

print("1.3.9")
water = 512.4
power = 1170
gas = 345.75
total = water + power + gas
print(f"Вода: {water:.2f} руб.")
print(f"Электричество: {power:.2f} руб.")
print(f"Газ: {gas:.2f} руб.")
print(f"Итого: {total:.2f} руб.") 

print("1.3.15")
visits = 350
buyers = 14
print(f"Посетители: {visits}")
print(f"Покупатели: {buyers}")
print(f"Конверсия: {buyers / visits * 100:.2f}%")

print("1.4.6")
name = "Анна"
age = 19
city = "Казань"
print("Имя;Возраст;Город")
print(f"{name};{age};{city}")

print("1.4.12")
print("Пн\tPython\tауд. 305")
print("Ср\tБазы данных\tауд. 210")
print("Пт\tСети\tауд. 118")

print("1.5.8")
gross_salary = 60000
tax = gross_salary * 0.13
net_salary = gross_salary - tax
daily_salary = net_salary / 22
print(f"Налог: {tax:.2f} руб.")
print(f"На руки: {net_salary:.2f} руб.")
print(f"За один день: {daily_salary:.2f} руб.")

print("1.5.11")
length = 5
width = 4
height = 2.7
wall_area = 2 * (length + width) * height
print(f"Площадь стен: {wall_area:.2f} кв. м")

print("1.5.15")
liters = 18
consumption = 7.5
distance = 300
possible_distance = (liters / consumption) * 100
remaining_distance = distance - possible_distance
print(f"Хватит на: {possible_distance:.2f} км")
print(f"Останется проехать: {remaining_distance:.2f} км")

print("1.6.11")
x = 1
y = 1
x += 1
y += 2
print(f"После хода 1: ({x}, {y})")
x += 2
y -= 1
print(f"После хода 2: ({x}, {y})")
