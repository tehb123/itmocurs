#coding utf-8
import os
dirname = 'C:/3/'
files = os.listdir(dirname)
print(files)
for name in files:
    fullname = os.path.join(dirname, name)
    with open(fullname, encoding='cp1251') as lst:
        spisok = []
        for line in lst:
            line = line.split()
            spisok.extend(line)
        print(spisok)
        fam = []
        nam = []
        for fam in spisok:
            fam = spisok[::2]
        for nam in spisok:
            nam = spisok[1::2]
        for p in nam:
            p = int(input("введите номер студента :"))
            print(fam[p-1], nam[p-1])
            break
        Dfam = dict()
        Dnam = dict()
        for word in fam:
            Dfam[word] = 'F'
        for word in nam:
            Dnam[word] = 'N'
        print(Dfam)
        print(Dnam)
import pickle


with open('data.pickle', 'wb') as f:
    pickle.dump(Dfam, f)
with open('data.pickle', 'rb') as f:
    Dfam_new = pickle.load(f)
    print(Dfam_new)


        #for d in nam:
        #    d = int(input("начало списка :"))
        #    f = int(input("конец списка :"))
        #    print(fam[d-1:f-1], nam[d-1:f-1])
        #    break

        #s = {}.fromkeys('f',fam[::1])

        #s = dict([x[1].strip().split(' ') for x in spisok])

        #print(s.keys())
        #print(s.items())
        #print(s.values())

        #print(s)




            #for i in range(len(fam)):
            #    print(fam[d-1:f-1], nam[d-1:f-1])
            #break
