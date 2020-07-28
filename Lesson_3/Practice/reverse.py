# Написать программу, которая выводит саму себя задом наперед
f = open("lesson3.py", "r")
for line in reversed(list(f)):
    print(line[::-1])