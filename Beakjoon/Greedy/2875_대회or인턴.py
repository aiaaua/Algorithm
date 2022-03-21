a, b, c = map(int, input().split())
cnt = 0

while True :
    a -= 2
    b -= 1
    if a < 0 or b < 0 or a+b < c :
        break
    cnt += 1
    
print(cnt)
