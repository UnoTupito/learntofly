EASY

1
def my_round(number, ndigits):
    number = str(number)
    number = number.split('.')
    number[1] = list(number[1])
    #print(number)
    if int(number[1][ndigits + 1]) >=5:
        number[1][ndigits:] = []
        number[1] = int(''.join(number[1])) + 1
        number[1] = str(number[1])
        if len(number[1]) > ndigits:
            number[1] = list(number[1])
            number[0] = int(number[0]) + 1
            number[0] = str(number[0])
            del number[1][0]
            number[1] = int(''.join(number[1]))

    else:
        number[1][ndigits:] = []
        number[1] = int(''.join(number[1]))
        #number[1] = int(number[1])

    result = str(number[0]) + '.' + str(number[1])
    result = float(result)
   # print(number)
    print(result)
    print(type(result))

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


2
def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)
    leftPart = ticket_number[:3]
    rightPart = ticket_number[3:]
    if len(rightPart) != 3:
        print('enter six numbers of your ticket')
    else:
        leftPart = list(leftPart)
        leftPart = [int(i) for i in leftPart]
        a = 0
        for k in leftPart:
            a +=k

        rightPart = list(rightPart)
        rightPart = [int(i) for i in rightPart]
        b = 0
        for k in rightPart:
            b +=k

        if a == b:
            print('ticket number ' + ticket_number + ' is lucky')
        else:
            print('ticket number ' + ticket_number + ' is not lucky')

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436752))


NORMAL

1
def fibonacci(n, m):
    fibo = [0, 1]
    while len(fibo) < m+1:
        fibo.append(fibo[-1] + fibo[-2])
    return fibo [n:m+1]

print(fibonacci(4, 7))


2
import random
myList1 = []
while len(myList1) <= 10:
    element = random.randint(0,20)
    myList1.append(element)

print('initial list is:')
print(myList1)

def sortMax (list):
    newList = []
    while len(list) > 0:
        a = min(list)
        newList.append(a)
        list.remove(a)
    return newList

myList2 = []
myList2 = sortMax(myList1)
print('The sorted list is:')
print(myList2)


3


4
A = []
A.append(int(input('Введите координату Х левого вверхнего угла')))
A.append(int(input('Введите координату У левого вверхнего угла')))

B = []
B.append(int(input('Введите координату Х правого вверхнего угла')))
B.append(int(input('Введите координату У правого вверхнего угла')))

C = []
C.append(int(input('Введите координату Х правого нижнего угла')))
C.append(int(input('Введите координату У правого нижнего угла')))

D = []
D.append(int(input('Введите координату Х левого нижнего угла')))
D.append(int(input('Введите координату У левого нижнего угла')))

def check (A, B, C, D):
    if B[0] - A[0] == C[0] - D[0] and A[1] - D[1] == B[1] - C[1]:
        return print('Ваша фигура является параллелограммом.')
    else:
        return print('Ваша фигура не является параллелограммом')

print(check(A, B, C, D))


