# -*- coding: utf-8 -*-

#w     以写方式打开，
#a     以追加模式打开 (从 EOF 开始, 必要时创建新文件)
#r+     以读写模式打开  从第一个开始写，覆盖 ，不删除
#w+     以读写模式打开 (参见 w )w+  覆盖写，删除原文件中的内容
#a+     以读写模式打开 (参见 a )  追加到后面


import os

os.system("ls -a")
f = open("t.txt","a+")
f.write("asdasa")

print f.readline()