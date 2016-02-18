#-*- coding: utf-8 -*-
import os
dirname = 'C:/2/'
files = os.listdir(dirname)
t = 0
print(files)
word = "python"
for name in files:
    fullname = os.path.join(dirname, name)
    if os.path.isfile(fullname):
        with open(fullname):
            if fullname.find(word) >=0 :
                t += 1
                print(fullname)
print(t)
#            for word in lstr.split():
#                if word in lstr:
#                    if lstr.find(word) != -1:

#                         t += 1
#                    else:
#                        continue
#            print(t, fullname)
#print(t)






#            spisok = []
#            for line in lst:
#                line = line.split()
##           print(spisok,fullname)             # n = d.count("python")
#            lst = fullname.split()
#            for a in range(0,len(lst)):
#                if lst.line.find(word) != -1:
#                    print ('dggd')


#for name in files:
#    fullname = os.path.join(dirname, name)
#    with open(fullname, encoding='cp1251') as lst:
#        spisok = []
#        for line in lst:
#            line = line.split()
#            spisok.extend(line)
#        print(spisok)