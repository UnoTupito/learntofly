EASY

1
fruitlist = ['banana', 'grapes', 'lemon', 'pear', 'apple']
for i, fruit in enumerate(fruitlist):
    print(i + 1, '{:>20}'.format(fruit))


2
import random
myList1 = []
while len(myList1) <= 10:
    element = random.randint(0,20)
    myList1.append(element)
myList2 = []
while len(myList2) <= 10:
    element = random.randint(0,20)
    myList2.append(element)
print('Первый список: ', myList1, 'Второй список: ', myList2)
i = 0
for check in myList1:
    if check in myList2:
        udoli = check
        myList1.remove(udoli) #почему-то без дополнительной переменной сразу с check работает некорректно
print('В первом списке осталось: ', myList1)


3
import random
listOriginal = []
while len(listOriginal) <= 10:
    element = random.randint(0,20)
    listOriginal.append(element)
print('The original list is the following:')
print(listOriginal)
listNew = []
for check in listOriginal:
    k = check % 2
    if k == 0:
        listNew.append(check / 4)
    else:
        listNew.append((check * 2))
print('The new list is the following:')
print(listNew)


NORMAL
1
import random
import math
list = []
n = int(input('How many numbers should it be in the list? '))
while len(list) <= n:
    add = random.randint(0,100)
    list.append(add)
print('The list is the following: ')
print(list)
newList = []
for check in list:
    k = math.sqrt(check)
    if (k).is_integer():
        newList.append(k)
if len(newList) == 0:
    print("no numbers with square root in the list")
else:
    print(newList)


2
date = input('Введите дату в формате дд.мм.гггг ')

dateList = date.split('.')

dayList = ['первое', 'второе', 'третье', 'четвёртое',
        'пятое', 'шестое', 'седьмое', 'восьмое',
        'девятое', 'десятое', 'одиннадцатое', 'двенадцатое',
        'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
        'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
        'двадцать первое', 'двадцать второе', 'двадцать третье',
        'двадацать четвёртое', 'двадцать пятое', 'двадцать шестое',
        'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
        'тридцатое', 'тридцать первое']

monthList = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
           'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']

day = dayList[int(dateList[0]) - 1]
month = monthList[int(dateList[1]) - 1]

print(day, month, dateList[2] + ' года')


3
import random
list = []
n = int(input('How many numbers should it be in the list?'))
while len(list) <= n:
    addNew = random.randint(-100,100)
    list.append(addNew)
print('Here is your list:')
print(list)


4
import random
import math

list = []
n = int(input('How many numbers should it be in the list? '))

while len(list) <= n:
    add = random.randint(0,20)
    list.append(add)
print('The list is the following: ')
print(list)

newList1 = []
i = 0
for check in list:
    if check not in newList1:
        newList1.append(check)
print(newList1) #список без повторюшек

newList2 = []

for check in list:
    k = list.count(check)
    if  k < 2:
        newList2.append(check)
print(newList2) #список с числами, которые встречаются только один раз