#!/usr/bin/env python3
# -*- coding: utf-8 -*-
m = int(input('Введите число от 1 до 7 '))
if m == 7:
    print('Воскресение')
elif m == 6:
    print('Суббота')
elif m == 5:
    print('Пятница')
elif m == 4:
    print('Четверг')
elif m == 3:
    print('Среда')
elif m == 2:
    print('Вторник')
elif m == 1:
    print('Понедельник')
else:
    print('Number not include in sequence 1-7')