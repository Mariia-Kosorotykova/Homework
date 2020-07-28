# Разбираемся, что делает функция zip,
# и пробуем написать свой собственный zip.
cities = ['Kharkiv', 'Kyiv', 'Dnipro']
schools = [301, 628, 256, 1234]
def shortest(*args):
    return range(len(sorted(args, key=len)[0]))

g = ((cities[i], schools[i]) for i in shortest(cities, schools) )

for item in g:
    print(item)
