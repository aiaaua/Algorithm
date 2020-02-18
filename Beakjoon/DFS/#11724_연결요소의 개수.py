import sys
sys.setrecursionlimit(1000000)

def dfs(i) :
    check[i] = True
    for line in lines :
        if i+1 == line[0] and not check[line[1]-1] : dfs(line[1]-1)
        elif i+1 == line[1] and not check[line[0]-1] : dfs(line[0]-1)
    
n, m = map(int, input().split())
lines = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(m)]
check = [False for _ in range(n)]
answer = 0

for i in range(n) :
    if not check[i] :
        dfs(i)
        answer += 1
        
print(answer)
