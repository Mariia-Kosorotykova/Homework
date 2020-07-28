# написать сумму списка при помощи цикла while
print('Please enter numbers:')
sum = 0
while True:
    n = int(input())
    if n == 0:
        break
    sum += n
print(sum)