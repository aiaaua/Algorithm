N, M = map(int, input().split())
num_list = range(1, N+1)
result = [0 for i in range(M)]
check = [0 for i in range(N)]

def solution(N, M, cnt, prev) :
    if cnt == M : 
        print(*result); return
    else : 
        for i in range(N) :
            if check[i] == 0 and num_list[i] >= prev:
                prev = num_list[i]
                result[cnt] = num_list[i]
                solution(N, M, cnt+1, prev)

solution(N, M, 0, 0)