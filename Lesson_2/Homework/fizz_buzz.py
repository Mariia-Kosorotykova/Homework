print('Hi! Enter please numbers:')
fizz = int(input())
buzz = int(input())
c = int(input())

for i in range(1, c + 1):
    if fizz == 0 or buzz == 0:
        print('Sorry, operations with zero are prohibited')
        break
    elif i % fizz == 0 and i % buzz == 0:
        print('FB', sep=' ', end=' ')
    elif i % fizz == 0:
        print("F", sep=' ', end=' ')
    elif i % buzz == 0:
        print('B', sep=' ', end=' ')
    else:
        print(i, sep=' ', end=' ')
print('\n Good luck!')
