# Вспоминаем работу с файлом. Есть файл, в котором много англоязычных текстовых
# строк. Считаем частоту встретившихся слов в файле, но через функции и map,
# без единого цикла!

#import re
f = open("words.txt", "r")
a = f.readlines()
result={}

def split_function (line):
    return line.split()
    #return re.split('[, .\s\n^$\W\b]', line)
def add_word(word):
    if word not in result:
        result[word] = 1
    else:
        result[word] += 1

def count_words(words_list):
    list(map(add_word, words_list))

a1 = list(map(split_function,a))
test = list(map(count_words, a1))
print(result)
#for word in f.read().split():
 #   if word not in wordcount:
 #       wordcount[word] = 1
 #  else:
 #       wordcount[word] += 1

#for k,v in wordcount.items():
 #   print(k,v)
#f.close();