# Создать словарь оценок предполагаемых студентов (Ключ - ФИ студента, значение - список оценок студентов).
# Найти самого успешного и самого отстающего по среднему баллу.

stud1 = 'vasya sidorov'
stud2 = 'ivan petrov'
stud3 = 'vasilina ivanova'
score1 = [3, 4, 5, 4, 3]
score2 = [5, 4, 5, 5, 4]
score3 = [3, 4, 5, 5, 4]

newdict = {'vasya sidorov': score1, 'ivan petrov': score2, 'vasilina ivanova': score3}

for keys, val in newdict.items():
 newdict[keys] = int(sum(val))/int(len(val))

print(max(newdict, key=newdict.get))
print(min(newdict, key=newdict.get))
