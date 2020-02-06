import sys

a = int(input())

time = [[0]*2 for _ in range(a)]

for i in range(a) :
    b, c = map(int, sys.stdin.readline().split())
    time[i][0] = b
    time[i][1] = c

time.sort(key = lambda x : (x[1], x[0]))

cnt = 1
end_time = time[0][1]

for i in range(1, a) : 
    if time[i][0] >= end_time :
        cnt += 1
        end_time = time[i][1]
        
print(cnt)
