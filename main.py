def myfunction(mystring):
    print(mystring)
    count = 0
    for i in mystring:
        if i == 'о':
            count += 1
    print('\nБуква "о" встречается', count, 'раз')


myfunction('''Не стоит прогибаться под изменчивый мир - 
Пусть лучше он прогнется под нас''')
