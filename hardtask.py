
import math
EPS = 1e-10
x = float(input('Введите значение x='))
s = x
n = 0
a = 0
while math.fabs(s) > EPS:
        s *= (((-1) ** n) * (x ** (2 * n + 1)))/(math.factorial((2 * n + 1) * (2 * n + 1)))
        a += s
        n += 1
        print(f"Si({x}) = {a}")