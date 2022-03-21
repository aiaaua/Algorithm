def dfs(start, depth) :
    if depth == 6 :
        print(' '.join(list(map(str, number))))
        return
    for i in range(start, len(L)) :
        number[depth] = L[i]
        dfs(i+1, depth+1)

number = [0 for _ in range(6)]

while True :
    L = list(map(int, input().split()))
    if L[0] == 0 : break
    del L[0]
    dfs(0, 0)
    print()
