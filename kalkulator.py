import logging
logging.basicConfig(level=logging.INFO)


def get_data():
    a = int(input('Podaj pierwsza liczbe'))  
    b = int(input('Podaj druga liczbe'))
    dzialanie = input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie')
    
    return a,b, dzialanie

def add(a,b):
    logging.info('Dodajemy {0} i {1} '.format(a, b))
    print('Wynik {0}'.format(a+b))

def sub(a,b):
    logging.info('Odejmujemy {0} i {1} '.format(a, b))
    print ('Wynik {0}'.format(a-b))

def multiply(a,b):
    logging.info('Mnozymy {0} i {1} '.format(a, b))
    print('Wynik {0}'.format(a*b))

def div(a,b):
    logging.info('Dzielimy {0} i {1} '.format(a, b))
    print ('Wynik {0}'.format(a/b))
   
def calculator():
    a,b, dzialanie = get_data()
    dict[dzialanie](a,b)

dict={
    '1': add,
    '2': sub, 
    '3': multiply,
    '4': div
}
calculator()
