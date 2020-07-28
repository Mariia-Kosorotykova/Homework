print('Please, enter number:')
a = int(input())
i=-1
while a>0:
    b = a%10
    a = a//10
    i+=1
    print(b, ' ', 10**i)