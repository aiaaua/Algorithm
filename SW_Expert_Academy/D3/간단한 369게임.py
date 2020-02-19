n = int(input())
num = 0
for i in range(1, n+1) :
    L = list(str(i))
    num = 0
    num = L.count("3") + L.count("6") + L.count("9")
    if num == 0 :
        print(i, '', end = '')
    else : 
        print('-' * num, '', end = '')
