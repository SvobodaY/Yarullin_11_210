#Найти сумму цифр введенного положительного целого числа.
number = int(input())
k = 0
a = [str(number)]
for i in a:
    for j in i:
        k += int(j)
print(k)