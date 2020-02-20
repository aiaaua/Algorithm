import collections

n, m = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(n)]

def bfs(i, j) :
    check[i][j] = True
    for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1) :
        nx, ny = i+dx, j+dy
        if 0<=nx<n and 0<=ny<m and not check[nx][ny] and [nx, ny] not in q and maze[nx][ny] == 1 :
            q.append([nx, ny])
            dist[nx][ny] = dist[i][j] + 1
    
dist = [[0 for _ in range(m)] for _ in range(n)]
dist[0][0] = 1
check = [[False for _ in range(m)] for _ in range(n)]
q = collections.deque()
q.append([0, 0])

while q : 
    [i, j] = q.popleft()
    if not check[i][j] :
        bfs(i, j)
        
print(dist[n-1][m-1])
