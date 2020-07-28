# Создать структуру данных для студентов из имен и фамилий, можно случайных.
# Придумать структуру данных, чтобы указывать, в какой группе учится студент
# (Группы Python, FrontEnd, FullStack, Java). Студент может учиться в нескольких группах. Затем вывести:
# студентов, которые не учатся на фронтенде
# студентов, которые изучают Python или Java

Python = {'vasya sidorov', 'ivan petrov'}
FrontEnd = {'vasilina ivanova'}
FullStack = {'vasilina ivanova', 'ivan petrov'}
Java = {'vasya sidorov', 'vasilina ivanova'}

listpy = list(Python)

allstud = Python | FrontEnd | FullStack | Java

# студентов, которые учатся в двух и более группах
print((Python & FullStack) | (FrontEnd & Java) | (Python & FrontEnd) | (Java & FullStack) | (Python & Java) | (FrontEnd & FullStack))

# студентов, которые не учатся на фронтенде
print(allstud - FrontEnd)

# студентов, которые изучают Python или Java
print(Java | Python)
