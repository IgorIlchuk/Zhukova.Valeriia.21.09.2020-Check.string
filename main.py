def myfunction(mystring):
    print(mystring)
    count = 0
    for i in mystring:
        if i == 'о':
            count += 1
    print('\nБуква "о" повторяеться', count, 'раз')


myfunction('''Не стоит прогибаться под изменчивый мир - 
Пусть лучше он прогнется под нас''')
