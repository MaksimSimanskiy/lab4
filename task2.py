#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('Решаем уравнение a•x²+b•x+c=0')
a = float(input('Введите значение a: '))
b = float(input('Введите значение b: '))
c = float(input('Введите значение c: '))

d = b ** 2 - 4 * a * c
print('Дискриминант = {}'.format(d))
if d == 0:
    x = -b / (2 * a)
    print('x = {}'.format(x))

else:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print('x₁ = {}'.format(x1))
    print('x₂ = {}'.format(x2))