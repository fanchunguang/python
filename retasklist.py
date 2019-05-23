# !/usr/bin/env python
# !-*-coding:utf-8 -*-
# !@Author : fanchg
# !@Time : 2018/8/8
import os
from distutils.log import warn as printf
import re

with os.popen('tasklist /nh', 'r') as f:  # \nh 去除每一列的标题
    for eachline in f:
        printf(re.findall(r'([\w.]+(?: [\w.]+)*)\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,] + K)', eachline.rstrip()))
f.close()


#  if __name__ == '__main__':
