S1 = "12345me"
S2 = "67890me"
s = S1 +S2
print (s)
print (s*3)

print (len(s)) # symbol

print (S1[0])

print (S1[-1])

print (s[3:6])

print (s[:6])

print (s[::3]) # step 3

f = s[:2]+"u"+s[2:] # срез
print (f)
start = 0
while True:
    i = s.find('me',start)
    if i < 0:
        break
    print (i)
    start = i+1

s = s.replace('me','gg')

print (s)
m = s.split('3')
print (m)

f1 ="python"
print (f1.upper())
if 'p' in f1:
    print (f1)

j = "В продвинутых отделениях почты все посылки и письма проходят через рентген," \
    " на подобие того, который стоит в аэропортах. В них различными цветами, помечены различны" \
    "е вещества, металлы, раст" \
    "воры веществ (лекарства, алкоголь), бумаги...деньги... Это часть меры безопасности против почтового терр" \
    "оризма» (из форума)" \
    "Согласно Федеральному Закону «О почтовой связи», № 176, от 17 июля 1999 года, статья № 22, на терр" \
    "итории нашей страны запрещены к пересылке деньги Российской Федерации и зарубежная валюта (это не от" \
    "носится к Центробанку России, а также его учреждениям)."

for i in j.split():
    i = i.replace (',','')
    if i.isdigit():
        print (i)

lst = [2,10,3,4,5]
print (lst[0])

print(len(lst))

print (lst[2:3])

print(lst.count(5)) #число в списка
lst.extend([0, 0, 0,])
print(lst)

lst.sort(key=lambda i:-i)
print(lst)
ls = ["f","dd","FFG","ds","авв"]
ls.sort()
print(ls)
