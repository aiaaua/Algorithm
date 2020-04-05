from collections import deque

C, B = map(int, input().split())
check=[False for _ in range(200001)]
time = 0
q = deque()
q.append(B)

while True :
    C += time
    
    if C > 200000 : return -1
    if check[C] : return time

    for i in range(len(q)) :
        present = q.popleft()
        
        move1 = present - 1
        if move1 >= 0 and not check[move1] :
            check[move1] = True
            q.append(move1)
        
        move2 = present + 1
        if move2 <= 200000 and not check[move2] :
            check[move2] = True
            q.append(move2)
        
        move3 = present * 2
        if move3 <= 200000 and not check[move3] :
            check[move3] = True
            q.append(move3)
        
    time +=1

# 라인에서 제시한 다른 테스트케이스 중 정답이 아닌 것도 있음
# 다시 풀어봐야 
