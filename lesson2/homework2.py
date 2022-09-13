#Вводятся вещественные x, y, целое n. 
#Определить, попадает ли в квадрат размера n c центром в начале координат точка (x, y)
x = float(input())
y = float(input())
n = int(input())
if x > n or y > n:
    print(False)
else:
    print(True)