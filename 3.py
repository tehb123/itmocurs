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
            nam = spisok [1::2]
        for p in nam:
            p = int(input("введите номер студента :"))
            print(fam[p-1], nam[p-1])
            break

        for d in nam:
            d = int(input("начало списка :"))
            f = int(input("конец списка :"))

            for i in range(len()):
                print(fam[d-1:f-1], nam[d-1:f-1])
            break




        #m = 1
        #spisAk = []
        #for spisAk in fam:
         #   fam [p] = spisAk [p] + nam [m]
          #  p = p + 1
           # m = m + 1
            #if p >= len(spisok):
             #   break
        #print(fam)
        #spisok = [0]+[1],[2]+[3],[4]+[5],[6]+[7],[8]+[9],[10]+[11],[12]+[13],[14]+[15],[16]+[17],[18]+[19],[20]+[21],[22]+[23],[24]+[25]
        #print (spisok)
    #lst = fullname.split()
    #print(lst
    #if os.path.isfile(l):
       # for i in fullname.split():
         #   if i.isalpha():
           #     print(i)