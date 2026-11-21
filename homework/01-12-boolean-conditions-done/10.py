att = int(input("Посещаемость, %: ")) >= 75
labs = int(input("Сдано лабораторных: ")) >= 8
no_debt = int(input("Долг по оплате, руб.: ")) == 0

print("Посещаемость:", att)
print("Лабораторные:", labs)
print("Нет долга:", no_debt)
print("Допущен:", att and labs and no_debt)
