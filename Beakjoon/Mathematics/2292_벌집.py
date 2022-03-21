n = int(input())
num, cnt = 1, 1

while True :
    if n <= num : print(cnt); break
    else : num += 6*cnt; cnt += 1
