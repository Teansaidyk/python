paid = input("Заказ оплачен (да/нет): ") == "да"
in_stock = input("Товар есть (да/нет): ") == "да"
has_address = input("Адрес указан (да/нет): ") == "да"

can_ship = paid and in_stock and has_address
need_call = paid and (not in_stock or not has_address)

print("Можно отправлять:", can_ship)
print("Позвонить покупателю:", need_call)
