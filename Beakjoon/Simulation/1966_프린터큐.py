from collections import deque

case_num = int(input())

for i in range(case_num) :
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    target = q[m]
    cnt = 0

    while q : 
        if max(q) > target : 
            while q[0] != max(q)  :
                q.append(q.popleft())
                m -= 1
            q.popleft()
            m -= 1
            cnt += 1
            if m < 0 : m += len(q) + 1
        elif max(q) == target :
            if q.count(target) != 1 :
                cnt += list(q)[:m].count(target)
            break
    print(cnt + 1)
