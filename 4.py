c = [c + d for c in 'list' if c != 'i' for d in 'spam' if d != 'a']
print(c)
c = list('listiii')
i = c.index('i', 2, 40)
print(i)

c.reverse()
print(c)

c = c[::-1]
print(c)

a = ('s',)

print (type(a))

d = dict.fromkeys(['a', 'b'], 100)   # ключ к нескольким значениям
print(d)

d = {a: a**2 for a in range(7)}             # range (7) создает список элементов от 0 до 7
print(d[5])

d['some key 112']=121

print(d)

print(d.get(3))          #d[3]
print(d.get(300, None))   # возможность задать значение по умолчанию
print(d.items())
print(d.keys(), len(d))          # all keys
#d.pop(3)      # извлекает 3

print(d.setdefault('112'))


print(d.values()) # все значения

d2 = {'113':'Hello'}
d.update(d2)
print(d)

#МНОЖЕСТВА добавлять только хеэшируемые элементы

a = set()
a={i**2 for i in range(7)}
print(4 in a)

a.symmetric_difference_update(d)
print(a)

#import pickle
#сделать базу данных

f = open('tttt','w') # открываем на запись
f.write('heel') # пишем
f.close() # CLOS

print(f.read())

