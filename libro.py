from os import listdir, curdir, rmdir, mkdir
from os.path import isdir, join

def showinsides():
    print('Имеются следующие директории:')
    for i in listdir(curdir):
        if isdir(join(curdir, i)):
            return print(i)

def deldir():
    showinsides()
    dirName = input('Введите название директории, которую нужно удалить.')
    try:
        rmdir(dirName)
        return print('Успешно удалено.')
    except OSError:
        return print('Что-то пошло не так. Удаление не выполнено.')

def newdir():
    dirName = input('Введите название директории, которую нужно создать.')
    try:
        mkdir(dirName)
        return print('Успешно создано.')
    except OSError:
        return print('Что-то пошло не так. Создать директорию не получилось.')
def opendir():
    showinsides()
    dirName = input('Введите название директории, которую нужно открыть.')
    try:
        print('В указанной вами папке содежатся:')
        print(listdir(dirName))
    except OSError:
        print('Что-то пошло не так. Не молучается отобразить содержимое указанной вами директории')