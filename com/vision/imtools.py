# !/usr/bin/env python
# !-*-coding:utf-8 -*-
# !@Author : fanchg
# !@Time : 2018/10/6

from PIL import Image
from pylab import *
import matplotlib.pyplot as plt
import os

def get_imlist(path):
    """返回目录中所有JPG图像的文件名列表"""
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]


# 读取图像到数组中
im = array(Image.open('d:\\picture\\data\\empire.jpg'))
# 绘制图像
plt.imshow()

# 一些点
x = [100, 100, 400, 400]
y = [200, 500, 200, 500]

# 使用红色星状标记绘制点
plt.plot(x, y, 'r*')

# 绘制连接前两个点的线
plt.plot(x[:2], y[:2])

title('Plotting : "empire.jpg"')

show()
axis('off')



