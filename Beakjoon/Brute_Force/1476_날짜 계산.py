E, S, M = map(int, input().split())
i = 1
while True :
    if E == 15 : E =0
    if S == 28 : S = 0
    if M == 19 : M = 0
    year = [E, S, M]
    temp = [i%15, i%28, i%19]
    if temp == year : print(i); break
    i += 1
