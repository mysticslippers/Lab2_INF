#Лабораторная работа №2
#Вариант №83
#Михайлов Дмитрий Андреевич
#Группа P3118
#Задание №9


n = input()
i, r = [], []
for k in range(len(n)):
    if str(k) in '013':
        r.append(int(n[k]))
    else:
        i.append(int(n[k]))
si = [r[0] ^ i[0] ^ i[1] ^ i[3], r[1] ^ i[0] ^ i[2] ^ i[3], r[2] ^ i[1] ^ i[2] ^ i[3]]
si.reverse()
s = ''.join([str(k) for k in si])
if s != '000':
    ind = 0
    s = s[::-1]
    for k in range(len(s)):
        ind += int(s[k]) * 2 ** k
    print('Ошибка в позиции: ' + str(ind))
    if str(ind) in '124':
        if r[ind // 2] % 2 == 0:
            r[ind // 2] = 1
        else:
            r[ind // 2] = 0
    elif ind == 3:
        if i[0] % 2 == 0:
            i[0] = 1
        else:
            i[0] = 0
    elif ind == 5:
        if i[1] % 2 == 0:
            i[1] = 1
        else:
            i[1] = 0
    elif ind == 6:
        if i[2] % 2 == 0:
            i[2] = 1
        else:
            i[2] = 0
    else:
        if i[3] % 2 == 0:
            i[3] = 1
        else:
            i[3] = 0
    print(''.join([str(k) for k in r[:2]]) + str(i[0]) + str(r[2]) + ''.join([str(k) for k in i[1:]]))
else:
    print('Ошибки нет!')
