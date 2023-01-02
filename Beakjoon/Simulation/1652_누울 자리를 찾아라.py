N = int(input())
room = [list(input()) for _ in range(N)]

length, width = 0, 0

for i in range(N):
    length_cnt, width_cnt = 0, 0
    for j in range(N):
        if room[i][j] == '.':
            length_cnt += 1
        else:
            if length_cnt >= 2:
                length += 1
            length_cnt = 0
            
        if room[j][i] == '.':
            width_cnt += 1
        else:
            if width_cnt >= 2:
                width += 1
            width_cnt = 0
        
        if j == N-1:
            if length_cnt >= 2:
                length += 1
            if width_cnt >= 2:
                width += 1

print(length, width)
