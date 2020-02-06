import itertools
N, M = map(int, input().split())
for i in list(itertools.product(range(1, N+1), repeat = M)) : print(*i)