from collections import deque

n, m = map(int, input().split())
q = deque(list(map(int, input().split())))
num_list = deque([i for i in range(1, n+1)])
cnt = 0

while q :
    target = q.popleft()
    idx = num_list.index(target)
    if idx < len(num_list) - idx :
        for i in range(idx) :
            tmp = num_list.popleft()
            num_list.append(tmp)
        cnt += idx
        num_list.popleft()
    else : 
        for i in range(len(num_list) - idx) :
            tmp = num_list.pop()
            num_list.appendleft(tmp)
        cnt += len(num_list) - idx
        num_list.popleft()
        
print(cnt)
