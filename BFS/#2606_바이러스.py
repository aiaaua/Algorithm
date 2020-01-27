numcom = int(input())
num_net = int(input())
networks = [[0 for _ in range(num_com + 1)] for _ in range(num_com + 1)]

for _ in range(num_net):
    x, y = map(int, input().split())
    networks[x][y] = 1; networks[y][x] = 1

def bfs(networks, start):
    q = [start]
    visited = []
    
    while q:
        std = q.pop(0)
        visited.append(std)
        for i in range(len(networks)): 
            if networks[std][i] and i not in visited and i not in q:
                q.append(i)
                
    return len(visited) - 1

print(bfs(networks, 1))