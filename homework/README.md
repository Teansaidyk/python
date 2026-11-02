# Переменные на входе (значения можно менять для проверки)
paint_price = 890
cans = 3
brush_price = 250
brushes = 2

# Расчет стоимости
paint_total = paint_price * cans
brushes_total = brush_price * brushes
total_sum = paint_total + brushes_total

# Вывод результатов в точном соответствии с примером
print(f"Краска: {paint_total} руб.")
print(f"Кисти: {brushes_total} руб.")
print(f"Всего: {total_sum} руб.")