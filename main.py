#Лабораторная работа №2
#Вариант №83
#Михайлов Дмитрий Андреевич
#Группа P3118
#Задание №9


n = input()   #Вводим число в двоичной системе счисления

r = [int(i) for i in n[4::]] #Делим строку на информационное сообщение и биты чётности
k = [int(i) for i in n[:4]]

si = [r[0] ^ k[0] ^ k[1] ^ k[3], r[1] ^ k[0] ^ k[2] ^ k[3], r[2] ^ k[1] ^ k[2] ^ k[3]]
s = ''.join([str(i) for i in si])

ind = 0
if s == '000':
    print(n)
    print("Нет ошибок.")
else:
    s = s[::-1]
    for i in range(len(s)):
        ind += int(s[i]) * 2 ** i
    ind = str(ind)
    print("Ошибка на позиции: " + ind)
    if ind in '124':
        if r[int(ind) // 2] % 2 == 0:
            r[int(ind) // 2] = 1
        else:
            r[int(ind) // 2] = 0
            print(''.join([str(i) for i in k]) + ''.join([str(i) for i in r]))
    else:
        if ind == '3':
            if k[0] % 2 == 0:
                k[0] = 1
            else:
                k[0] = 0
        elif ind == '5':
            if k[1] % 2 == 0:
                k[1] = 1
            else:
                k[1] = 0
        elif ind == '6':
            if k[2] % 2 == 0:
                k[2] = 1
            else:
                k[2] = 0
        else:
            if k[3] % 2 == 0:
                k[3] = 1
            else:
                k[3] = 0
        print(''.join([str(i) for i in k]) + ''.join([str(i) for i in r]))
