numbers = input().split()
number = int(input())


low = 0
high = len(numbers) - 1
mid = (low + high) // 2


while number != int(numbers[mid]):
    if number > int(numbers[mid]):
        low = mid + 1
    else: 
        high = mid - 1
    mid = (low + high) // 2


print(mid)