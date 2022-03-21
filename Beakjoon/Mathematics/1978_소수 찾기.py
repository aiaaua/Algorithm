case_num = int(input())
num = list(map(int, input().split()))
cnt = 0

for i in range(case_num) :
    if num[i] == 1 : continue
    for j in range(2, num[i]) :
        if num[i]%j == 0 : break
    else : cnt += 1

print(cnt)
