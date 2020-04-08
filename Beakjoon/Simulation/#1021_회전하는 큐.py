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
            num_list.append(num_list.popleft())
        cnt += idx
        num_list.popleft()
    else : 
        for i in range(len(num_list) - idx) :
            num_list.appendleft(num_list.pop())
        cnt += len(num_list) - idx
        num_list.popleft()
        
print(cnt)
