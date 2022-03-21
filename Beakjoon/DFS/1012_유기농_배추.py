import sys
sys.setrecursionlimit(10000)

def get_num_earthwarm():
    earthwarm = 0
    for i in range(n):
        for j in range(m):
            if farm[i][j] and not check[i][j]:
                dfs(i, j)
                earthwarm += 1
    print(earthwarm)

def dfs(i, j):
    check[i][j] = True
    
    for dx, dy in (-1,0), (1,0), (0,1), (0,-1):
        nx, ny = i+dx, j+dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if farm[nx][ny] and not check[nx][ny]:
            dfs(nx, ny)


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    farm = [[0]*m for _ in range(n)]
    check = [[False]*m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        farm[y][x] = 1
        
    get_num_earthwarm()
