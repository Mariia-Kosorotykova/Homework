#Написать fizzbuzz для 20 троек чисел, которые записаны в файл.
#Читаете из файла первую строку, берете из нее числа, считаете для них fizzbuzz,
#результат пишется в другой файл.

f = open("numbers.py", "r")
f_d = open("demofile.py", "w")
for line in f.readlines():
    k = line.split()
    fizz = int(k[0])
    buzz = int(k[1])
    c = int(k[2])
    for i in range(1, c + 1):
        if fizz == 0 or buzz == 0:
            f_d.write("Sorry, operations with zero are prohibited")
            break
        elif i % fizz == 0 and i % buzz == 0:
            f_d.write(" FB ")
        elif i % fizz == 0:
            f_d.write(" F ")
        elif i % buzz == 0:
            f_d.write(" B ")
        else:
            f_d.write(" " +str(i))
    f_d.write('\n')
f.close()
f_d.close()