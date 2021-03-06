# !/usr/bin/env python
# !-*-coding:utf-8 -*-
# !@Author : fanchg
# !@Time : 2018/8/8
from random import randrange,choice
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime

tlds = ('com', 'edu', 'net', 'org', 'gov')

for i in range(randrange(5, 11)):
    dtint = randrange(2**32)      # pick date
    dtstr = ctime(dtint)
    llen = randrange(4, 8)          # login is shorterq
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)      # domain is longer
    dom = ''.join(choice(lc) for j in range(dlen))
    print('%s::%s@%s.%s::%d-%d-%d' % (dtstr, login, dom, choice(tlds), dtint, llen, dlen))


