target = int(input())
a = target
cnt = int()

while True :
    cnt += 1
    a = (a%10)*10 + (a//10 + a%10)%10
    if a == target : break
print(cnt)
