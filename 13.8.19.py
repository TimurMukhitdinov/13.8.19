print('Введите количество билетов')
x = int(input())
counter_price = 0
counter_peoples = 0
for i in range(1, x + 1):
    counter_peoples += 1
    print('Введите возраст посетителя')
    age = int(input())
    if age < 18:
        counter_price += 0
    elif 18 <= age <= 24:
        counter_price += 990
    else:
        age <= 25
        counter_price += 1390
if 3 <= counter_peoples:
    counter_price *= 0.9
    print('Гостей более 3-х.', 'Вам Предоставляется дополнительная скидка 10%.', sep='\n')
    print('Цена со скидкой =', counter_price, 'руб.')
else:
    print('Общая сумма вашего заказа', counter_price, 'руб.')