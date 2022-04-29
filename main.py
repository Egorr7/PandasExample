
import numpy
import pandas
from colorama import init
from colorama import Fore, Back, Style

init(autoreset=True)

dataframe = pandas.read_csv('data/data01.csv', delimiter=';', names=['date', 'event', 'country', 'user_id', 'source', 'topic'])
print(Fore.GREEN + 'Первые 5 строк\n', dataframe.head())
print('==========')
print(Fore.GREEN + 'Последние 5 строк\n', dataframe.tail())
print('==========')
print(Fore.GREEN + 'Случайные 5 строк\n', dataframe.sample(5)) # Случайные 5 строк
print('==========')
print(Fore.GREEN + 'Выборка по столбцам\n', dataframe[['country', 'user_id']]) # Случайные 5 строк

print('==========')
print(Fore.GREEN + 'Вывод определённых колонок\n')
print(dataframe.user_id) # or dataframe['user_id']
print('==========')
print(Fore.GREEN + '1) Фильтрация определенных значений\n')
print(dataframe.source == 'SEO')
print(Fore.GREEN + '2)')
print(dataframe.source[dataframe.source == 'SEO'])