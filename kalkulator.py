import logging
logging.basicConfig(level=logging.INFO)

print ('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie') 
a = int(input('Podaj pierwsza liczbe'))  
b = int(input('Podaj druga liczbe'))
dzialanie=input('Wybierz dzialanie jakie chcesz wykonac')

if dzialanie == '1':
    wynik=a+b
    logging.info('Dodajemy {0} i {1} '.format(a, b))
elif dzialanie == '2':
    wynik=a-b
    logging.info('Odejmujemy {0} i {1} '.format(a, b))
elif dzialanie == '3':
    wynik= a*b
    logging.info('Mnozymy {0} i {1} '.format(a, b))
elif dzialanie == '4':
    wynik =a/b
    logging.info('Dzielimy {0} i {1} '.format(a, b))
print(wynik)



