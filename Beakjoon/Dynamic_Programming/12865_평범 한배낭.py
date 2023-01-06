N, K = map(int, input().split())
stuff = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
knapsack = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        weight, value = stuff[i]

        if j < weight:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(knapsack[i-1][j], value + knapsack[i-1][j-weight])

print(knapsack[N][K])
