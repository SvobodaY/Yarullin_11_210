#Подсчитать сумму слагаемых (k! * x^k) для k от 1 до n. x - вещественное.
x = float(input())
n = int(input())
count = 0
for k in range(1, n + 1):
    count += 1
print(count)