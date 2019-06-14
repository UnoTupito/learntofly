EASY

1
import os

i = 1
while i < 9:
    dirName = 'dir_' + str(i)
    os.mkdir(dirName)
    i += 1

i = 1
while i < 9:
    dirName = 'dir_' + str(i)
    os.rmdir(dirName)
    i += 1


2
from os import listdir
from os.path import join
from os import curdir
from os.path import isdir


for i in listdir(curdir):
    if isdir(join(curdir, i)):
        print(i)


3
import os
import shutil
path = os.mkdir('copies')
shutil.copy(__file__, 'copies')

