# Задание №1
hello = 'Добрый день'
home_work = 'Это моё первое домашнее задание'
you_name = input("Введите Ваше имя: ")
you_age = int(input("Укажите Ваш возвраст: "))
print(f"{hello}, {you_name}. {home_work} Ваш возраст {you_age}.")

# Задание №2
time = int(input("Введите время в секундах: "))
hour = time // 3600
minutes = (time - (hour * 3600)) // 60
sec = time - ((hour * 3600) + (minutes * 60))
print(f"{hour}:{minutes}:{sec}")

# Задание №3
numb = input('Введите число: ')
print(int(numb) + int(str(numb + numb)) + int(str(numb + numb + numb)))

# Задание №4
BASE = 10
user_number = int(input('Введите положительное целое число: '))
maximum = 0
while user_number:
    digit = user_number % BASE
    if digit > maximum:
        maximum = digit
    user_number //= BASE
print('Максимальное число:', maximum)

# Задание №5
revenue = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))
profit = revenue - costs
lesion = costs - revenue
if revenue > costs:
    print(f"Финансовый показатель положительный. Прибыль составляет: {profit}.")
else:
    print(f"Финансовый показатель отрицательный. Убыток составляет: {lesion}.")

# Задание №6
revenue = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))
profit = revenue - costs
lesion = costs - revenue
profitability = profit / revenue
if revenue > costs:
    print(f"Финансовый показатель положительный. Прибыль: {profit}.\nРентабельность: {profitability}")
    staff = int(input('Сколько сотрудников в Вашей фирме? '))
    profit_human = profit / staff
    print(f'Прибыль на одного сотрудника в Вашей фирме составляет: {profit_human:.1f}')
else:
    print(f"Финансовый показатель отрицательный. Убыток составляет: {lesion}.")

# Задание №7
distance = int(input('Сколько км Вы пробежали за первый день? '))
maxx = int(input('Не менее скольки км необходимо пробежать? '))
i = 0.1
day = 2
while distance <= maxx:
    distance = (distance * i) + distance
    print(f'{day}: {distance:.1f}')
    day = day + 1
    if distance >= maxx:
        day = day - 1
        print(f'На {day} день Вы достигните результата не менее - {maxx} км.')
