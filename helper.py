import libro

wish = int(input('Выберете действие:'
                 '1 - перейти в папку'
                 '2 - посмотреть содержимое текущей папки'
                 '3 - удалиь папку'
                 '4 - создать папку'))

if wish == 1:
    libro.opendir()
elif wish == 2:
    libro.showinsides()
elif wish == 3:
    libro.deldir()
elif wish == 4:
    libro.newdir()
else:
    print('Нужно ввести число от 1 до 4')



