from collections import deque
while True :
    w, h = map(int, input().split())
    if w == 0 and h == 0 : break
    
    mapp = [list(map(int, input().split())) for _ in range(h)]
    check = [[False] * w for _ in range(h)]
    q = deque()
    cnt = 0
    for i in range(h) :
        for j in range(w) :
            if mapp[i][j] == 1 and not check[i][j] :
                q.append([i, j])
                while q :
                    x, y = q.popleft()
                    check[x][y] = True
                    for nx, ny in (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1) :
                        dx, dy = x+nx, y+ny
                        if 0<=dx<h and 0<=dy<w :
                            if mapp[dx][dy] == 1 and not check[dx][dy] : q.append([dx, dy]); check[dx][dy] = True
                cnt += 1
    print(cnt)
