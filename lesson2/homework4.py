#Вводится вещественные x, y. Определить, 
#попадает ли точка в мишень (концентрические круги радиусом 1, 2, ... 10). 
#Если да, то вывести номер круга наименьшего радиуса, куда попала точка. Если не попадает, то вывести "missed".
x, y = float(input()), float(input())
mintarget = 11
for i in range(1, 11):
    if ((x ** 2 + y ** 2) ** 0.5) < i:
        if i < mintarget:
            mintarget, i = i, mintarget
if mintarget == 11:
    print('missed')
else:
    print(mintarget)