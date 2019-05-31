Тульгук Елена
EASY

3
age = int(input('Сколько вам лет?'))
if age >= 18:
    print('Добро пожаловать!')
else:
    print('Извините, пользование данным ресурсом только с 18 лет.')


2
number = int(input('enter a number'))
while number >= 1:
    remainder = number % 10
    number = number // 10
    print(remainder)
print('Your number consists of the digits above')


1
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
helpNum = num1
num1 = num2
num2 = helpNum
print('Now the first number is ' + str(num1) + ' and the second number is 5' + str(num2))


NORMAL

1
number = int(input('enter a number'))
biggestDigit = 0
while number >= 1:
    remainder = number % 10
    number = number // 10
    if remainder > biggestDigit:
        biggestDigit = remainder
        continue
print('The biggest digit in your number is ' + str(biggestDigit))


2
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print('Now the first number is ' + str(num1) + ' and the second number is ' + str(num2))5


3
a = int(input('Введите коэфициент a: '))
b = int(input('Введите коэфициент b: '))
c = int(input('Введите коэфициент c: '))

import math
D = b ** 2 - 4 * a * c
if D < 0:
    print('Уравнение корней не имеет.')
elif D == 0:
    b = 0 - b
    x = (b + math.sqrt(D)) / (2 * a)
    print('Корень данного квадратного уравнения равен ' + str(x))
elif D > 0:
    b = 0 - b
    x1 = (b + math.sqrt(D)) / (2 * a)
    x2 = (b - math.sqrt(D)) / (2 * a)
    print('Корни данного квадратного уравнения: ' + str(x1) + 'и' + str(x2))

