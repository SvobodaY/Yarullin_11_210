#Вывести таблицу умножения цифр от 2 до 9 - в виде таблицы.
for x in range(2, 10):
    for j in range(1, 11):
        print(x, 'x', j, '=', x * j, end='\n')
    print('')
    