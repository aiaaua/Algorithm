import sys
sys.setrecursionlimit(1000000)

def dfs(i, j, h) :
    check[i][j] = True
    for dx, dy in (1, 0), (-1, 0), (0, -1), (0, 1) :
        nx, ny = i+dx, j+dy
        if (0 <= nx < n) and (0 <= ny < n) :  
            if region[nx][ny] > h and not check[nx][ny] :
                dfs(nx, ny, h)

n = int(input())
region = [list(map(int, input().split())) for _ in range(n)]
max_num = max([max(region[i]) for i in range(n)])
safe_region = [0]

for h in range(max_num) :
    check = [[False]*n for _ in range(n)]
    num_region = 0
    
    for i in range(n) :
        for j in range(n) :
            if region[i][j] > h and not check[i][j] :
                dfs(i, j, h)
                num_region += 1
    safe_region.append(num_region)

print(max(safe_region))