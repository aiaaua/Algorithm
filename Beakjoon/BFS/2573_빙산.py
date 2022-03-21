import sys
from collections import deque

def bfs(i, j) :
    check[i][j] = True
    q.append([i, j])
    
    while q :
        zeros = 0
        i, j = q.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, 1), (0, -1) :
            nx, ny = i+dx, j+dy
            if (0<=nx<n) and (0<=ny<m) and not check[nx][ny]:
                if iceberg[nx][ny] != 0 :
                    check[nx][ny] = True; q.append([nx, ny])
                else : zeros += 1
        n_iceberg[i][j] = max(iceberg[i][j]-zeros, 0)
        
n, m = map(int, sys.stdin.readline().split())
iceberg = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
q = deque()
year = 0

while True :
    cnt = 0
    check = [[False]*m for _ in range(n)]
    n_iceberg = [[0]*m for _ in range(n)]
    
    for i in range(n) :
        for j in range(m) :
            if iceberg[i][j] != 0 and not check[i][j] : bfs(i, j); cnt += 1
    
    if cnt == 0 : year = 0; break
    elif cnt >= 2 : break
    year += 1; iceberg = n_iceberg

print(year)
