import itertools
N, M = map(int, input().split())
for i in list(itertools.combinations_with_replacement(range(1, N+1), M)) : print(*i)
