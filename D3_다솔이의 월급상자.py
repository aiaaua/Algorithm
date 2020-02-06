T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    sal = 0
    for i in range(N) :
        p, x = map(float, input().split())
        sal += p*x
    print('#{0} {1}'.format(test_case, sal))