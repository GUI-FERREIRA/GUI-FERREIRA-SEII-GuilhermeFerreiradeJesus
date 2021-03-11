#funções
def funcao1():
    print('Hello, funcao 1')

def funcao2(greeting):
    return '{} Function.'.format(greeting)

def funcao3(greeting, name ='you'):
    return '{}, {}'.format(greeting, name)

def funcao4(*args, **kwargs):
    print(args)
    print(kwargs)


month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def funcao5(year):
    """Retorna True para anos bissextos, False para anos não bissextos."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def funcao6(year, month):
    """Retorna o número de dias daquele mês naquele ano."""
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month == 2 and funcao5(year):
        return 29
    return month_days[month]

#funcao1()
#print(funcao2('ola'))
#print(funcao3('ola'))
#funcao4('math', 'art', name='guilherme', age =22)
#help(funcao5)
#print(funcao5(2020))
#help(funcao6)
#print(funcao6(2020, 2))

