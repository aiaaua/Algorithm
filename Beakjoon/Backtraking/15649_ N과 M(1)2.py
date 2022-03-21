N, M = map(int, input().split())
num_list = range(1, N+1)
result = [0 for i in range(M)]
check = [0 for i in range(N)]

def solution(N, M, cnt) :
    if cnt == M : 
        print(*result); return
    else : 
        for i in range(N) :
            if check[i] == 0 :
                check[i] = 1
                result[cnt] = num_list[i]
                solution(N, M, cnt+1)
                check[i] = 0

solution(N, M, 0)