# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.
num = int(input('Введите месяц года: '))
my_dict = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
my_dict2 = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь', 7: 'июль', 8: 'август', 9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}

if num in sum(my_dict.values(), []):
    for i in my_dict.items():
        if num in i[1]:
            print('Этому месяцу соответствует', i[0].lower(), {my_dict2[num]})

# Вариант 2 - с месяцами:
my_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
if num in my_dict2:
    print(f'{num}-й месяц года - это {my_list[num - 1]}')
    print(f'{num}-й месяц года - это {my_dict2[num]}')


