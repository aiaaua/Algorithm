for _ in range(int(input())) : 
    a, b = map(int, input().split())

    if a <= b : large, small  = b, a
    else : large, small = a, b

    while small != 0 :
        large = large%small
        large, small = small, large

    print(int(a*b/large))
