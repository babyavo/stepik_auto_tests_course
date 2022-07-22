s_ua = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
s_en = 'abcdefghijklmnopqrstuvwxyz'

s = str(input("Введіть рядок літер: ")).lower().strip() # Рядок літер
key = int(input("Введіть ключ: "))  # Зсув літер
n = int(input('Оберіть мову 1 - українська, 2 - англійська: '))

def code(s, key, n, l):
    global new1
    new1 = ''
    for i in s:
        e = n.index(i) + key
        if e >= l:
            e -= l
        if e < 0:
            e += l
        new1 += n[e]
    return new1

def decode(s, key, n, l):
    new2 = ''
    for i in s:
        e = n.index(i) - key
        if e < 0:
            e += l
        elif e >= l:
            e -= l
        new2 += n[e]
    return new2

if n == 1:
    l = len(s_ua)
    print("Закодоване повідомлення: ", code(s, key, s_ua, l))
    print("Декодоване повідомлення: ", decode(new1, key, s_ua, l))
elif n == 2:
    l = len(s_en)
    print("Закодоване повідомлення: ", code(s, key, s_en, l))
    print("Декодоване повідомлення: ", decode(new1, key, s_en, l))

