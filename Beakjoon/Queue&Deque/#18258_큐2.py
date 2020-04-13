import sys
from collections import deque

num = int(input())
commend = [list(sys.stdin.readline().split()) for _ in range(num)]
q = deque()

for i in range (num) :
    if commend[i][0] == "push" : q.append(commend[i][1])
    elif commend[i][0] == "pop" :
        if len(q) >= 1 : print(q.popleft())
        else : print(-1)
    elif commend[i][0] == "size" : print(len(q))
    elif commend[i][0] == "empty" :
        if len(q) == 0 : print(1)
        else : print(0)
    elif commend[i][0] == "front" :
        if len(q) >= 1 : print(q[0])
        else : print(-1)
    elif commend[i][0] == 'back' :
        if len(q) >= 1 : print(q[-1])
        else : print(-1)
