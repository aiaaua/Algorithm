for j in range(1, 11) :
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(2, n-2) :
        g = h[i] - max(h[i-2], h[i-1], h[i+1], h[i+2])
        if g > 0 : ans += g
        
    print('#{0} {1}'.format(j, ans))
