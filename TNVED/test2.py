with open("C:\Users\Пользователь\Documents\хкатон от 15\TNVED\TNVED4.Txt", encoding='cp866') as fout_tnved2:
    lst = []
    fout_tnved2.readline()
    for line in fout_tnved2.readlines():
        line = line.replace('\xa0', '')
        ls = line.split('|')
        ls.pop(-1)
        lst.append(ls)
    for x in range(len(lst)):
        for i in range(x+1, len(lst)):
            if lst[x][1] in lst[i]:
                del lst[x]
                break