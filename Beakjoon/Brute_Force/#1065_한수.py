cnt = 0

for i in range(1, int(input())+1) :
    if i <= 99 : cnt += 1
    else :
        L = list(map(int, str(i)))
        if L[2]-L[1] == L[1]-L[0] : cnt += 1

print(cnt)
