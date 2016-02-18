import sys, os
def newfunc():
    def add(x, y):
         return x + y
    return add
def func():
    pass
print(func())

def summ(lst):
    summa = 0
    for a in lst:
        summa += a
    return summa
lst = {2, 4}
ret = summ(lst)
print(ret)

def some_file_work(text):
    f = open('rrr.txt', 'a')
    s = "{}\n".format(text)
    f.write(s)
    f.close()
some_file_work("heelo")
some_file_work("mu")

# аргументы функции

def func1(a, b, c=2 ):
    return a+b+c
ret = func1(10, 20, 30)
print(ret)

def debug(*args):
    for a in args:
        print(a)
    return args


print(debug(1,2,3))

#def debug1(**kwargs):
#    if kwargs['pass'] == '19':
#        print('имя',kwargs['name'])
#    return kwargs
#debug1(name = "iv")

#def paint(a):
#    s = "{}".format(a)
#    return paint
#paint("ggg")

print("hhh=",(lambda x, y: x + y)#add = lambda x, y: x + y
(10,20))

lst = [
    ['ivan','novikov'],
    ['maris','Kozevnikova'],
    ['Will','smith']
]

#lst.sort( key=lambda lst2: lst2[1])


#print((lambda name,lastname:len(name)/len(lastname))(lst[0][0],lst[0][1]))
#koef=lambda name,lastname:len(name)/len(lastname)
koef = lambda lst:[len(a[0])/len(a[1]) for a in lst]

for name, lastname in lst:
#    print(name,koef(name,lastname))
#print(koef(lst))&&&&&&

