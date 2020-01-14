def change(box, loc,r,c) :
    n_loc = collections.deque()
    while len(loc) != 0 :
        std = loc.popleft()
        if std[0] > 0  and box[std[0]-1][std[1]] == 0 :
            n_loc.append([std[0]-1, std[1]])
            box[std[0]-1][std[1]] = 1
        if std[0] < r-1 and box[std[0]+1][std[1]] == 0 :
            n_loc.append([std[0]+1, std[1]])
            box[std[0]+1][std[1]] = 1
        if std[1] > 0 and box[std[0]][std[1]-1] == 0 :
            n_loc.append([std[0], std[1]-1])
            box[std[0]][std[1]-1] = 1
        if std[1] < c-1 and box[std[0]][std[1]+1] == 0 :
            n_loc.append([std[0], std[1]+1])
            box[std[0]][std[1]+1] = 1
    return box, n_loc

def get_zero(box) :
    cnt = 0
    for i in box :
        cnt += i.count(0)
    return cnt

def BFS() :
    import sys
    import collections
    
    c,r = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(r)]
    loc = collections.deque()
    day = 0

    for i in range(r) :
        for j in range(c) :
            if box[i][j] == 1 :
                loc.append([i, j])
                
    while True :
        zeros = get_zero(box)

        if zeros != 0 :
            box, loc = change(box, loc,r,c)
            day+=1
            n_zeros = get_zero(box)
            if n_zeros == 0 :
                return day
                break
            elif n_zeros == zeros :
                return -1
                break
        
BFS()
