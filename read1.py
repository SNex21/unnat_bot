def create_db():
    a = open('1.txt', encoding='utf-8').readlines()
    k = []
    for i in a:
        k.append(i.split('.\t')[1][:-1])
    return k