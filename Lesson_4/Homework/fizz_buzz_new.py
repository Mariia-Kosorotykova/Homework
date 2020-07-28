#Написать fizzbuzz для 20 троек чисел, которые записаны в файл.
#Читаете из файла первую строку, берете из нее числа, считаете для них fizzbuzz,
#результат пишется в другой файл.
#украшаем работу физбазов работой со строками, списками, пробуем генераторы списков
#и прочие новые красоты, которые выучили. Доводим код до идеала!

f = open("numbers.py", "r")
f_d = open("demofile.py", "w")
for line in f.readlines():
    fizz, buzz, c = [int(el) for el in line.split()]
    for i in range(1, c + 1):
        if not fizz or not buzz:
            f_d.write('Sorry, operations with zero are prohibited')
            break
        elif not i % fizz and not i % buzz:
            f_d.write(' FB ')
        elif not i % fizz:
            f_d.write(' F ')
        elif not i % buzz:
            f_d.write(' B ')
        else:
            f_d.write(' %s' % (i))
    f_d.write('\n')
f.close()
f_d.close()