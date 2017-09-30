#!/usr/bin/python2.7
# -*- coding: utf-8 -*-



l=[2121,'wqwq']

print len(l)

print l.__len__()
# 循环
for a in l:
    print a

print l[0]

print l[:-1]

c= l+[46,5453,'rwerwe']

print c[2]

l.append(12121)

print l[2]

print l.pop(2)
print l