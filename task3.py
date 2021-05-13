#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
n = int(input('Введите значение n от 1 до 4: '))
if(n < 1 or n > 4):
    print("Число вне интервала")
    exit(1)
a = math.pow(10, n - 1)
b = math.pow(10, n) - 1
s = (b * (b + 1) - a * (a - 1)) / 2
print('Результат = {}'.format(s))
