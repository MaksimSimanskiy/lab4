a = int(input('Enter first side '))
b = int(input('Enter second side  '))
c = int(input('Enter third side  '))
if a + b <= c or a + c <= b or b + c <= a:
    print("Треугольник не существет")
elif a != b and a != c and b != c:
    print("Разносторонний")
elif a == b == c:
    print("Равносторонний")
else:
    print("Равнобедренный")