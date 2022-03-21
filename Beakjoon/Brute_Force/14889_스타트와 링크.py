from itertools import combinations

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
minimum = float('inf')

for comb in combinations([i for i in range(n)], n//2) :
    s_cases = combinations(list(comb), 2)
    l_cases = combinations([i for i in range(n) if i not in comb], 2)
    
    s_sum, l_sum = 0, 0
    
    for s_case in s_cases : s_sum += matrix[s_case[0]][s_case[1]] + matrix[s_case[1]][s_case[0]]
    for l_case in l_cases : l_sum += matrix[l_case[0]][l_case[1]] + matrix[l_case[1]][l_case[0]]
        
    if minimum > abs(s_sum - l_sum) : minimum = abs(s_sum - l_sum)

print(minimum)
