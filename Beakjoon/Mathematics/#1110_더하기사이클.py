import copy

target = int(input())
a = copy.deepcopy(target)
cnt = 0

while True :
    cnt += 1
    a = (a%10)*10 + (a//10 + a%10)%10
    if a == target : print(cnt);break