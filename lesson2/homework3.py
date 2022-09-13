#Вводятся вещественные x, y, целое n. 
#Определить, попадает ли в круг радиуса n c центром в начале координат точка (x, y)
x, y = float(input()), float(input())
n = int(input())
if (x ** 2 + y ** 2) ** 0.5 < n:
    print(True)
else:
    print(False)