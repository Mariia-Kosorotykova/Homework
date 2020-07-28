# Написать программу, которая выводит саму себя
import sys
lesson3 = sys.argv[0]
f = open(lesson3, 'r')
for line in f:
	print(line)
f.close()