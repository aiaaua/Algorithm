from itertools import combinations

for _ in range(int(input())) :
    num = list(map(int, input().split()))
    cases = list(combinations(num[1:], 2))
    gcd_sum = 0
    for case in cases : 
        large, small = 0, 0
        if case[0] >= case[1] : large, small = case[0], case[1]
        else : large, small = case[1], case[0]
        while small != 0 :
            large = large%small
            large, small = small, large
        gcd_sum += large
    print(gcd_sum)
