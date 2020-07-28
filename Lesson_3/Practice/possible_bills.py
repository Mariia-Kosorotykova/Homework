#Банкомат выдает сумму максимально возможными купюрами
print("Please, enter sum:")
a = int(input())
v = [1000, 500, 200, 100, 50, 20, 10]
for i in v:
        print(str(a//i), i)
        a -= a//i * i