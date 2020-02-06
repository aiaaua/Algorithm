import sys
import queue

size = int(sys.stdin.readline())
data = [[int(i) for i in input()] for _ in range(size)]

def BFS(data, size) :
    q = queue.Queue()
    out = []
    cnt = []

    for i in range(size) :
        for j in range(size) :
            if data[i][j] != 0 :
                q.put([i, j])
                data[i][j] = 0
                while q.qsize() != 0 :
                    std = q.get()
                    out.append(std)
                    if std[0] > 0  and data[std[0]-1][std[1]] != 0 :
                        q.put([std[0]-1, std[1]])
                        data[std[0]-1][std[1]] = 0
                    if std[0] < size-1 and data[std[0]+1][std[1]] != 0 :
                        q.put([std[0]+1, std[1]])
                        data[std[0]+1][std[1]] = 0
                    if std[1] > 0 and data[std[0]][std[1]-1] != 0 :
                        q.put([std[0], std[1]-1])
                        data[std[0]][std[1]-1] = 0
                    if std[1] < size-1 and data[std[0]][std[1]+1] != 0 :
                        q.put([std[0], std[1]+1])
                        data[std[0]][std[1]+1] = 0


                cnt.append(len(out))
                out = []
                
    print(len(cnt))
    for i in range(len(cnt)) :
        print(cnt[i])
                        
                        
BFS(data, size)
