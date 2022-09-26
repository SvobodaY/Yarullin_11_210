# Подсчитать сумму n^1 + n^2 + ... + n^n для введенного натурального n.
n = int(input())
k = 1
count = 0
while k <= n:
    count = count + (n ** k)
    k += 1
print(count)