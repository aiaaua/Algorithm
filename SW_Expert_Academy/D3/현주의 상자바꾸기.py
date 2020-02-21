for case in range(1, int(input())+1) : 
    n, q = map(int, input().split())
    boxes = [0 for _ in range(n)]
    changes = [list(map(int, input().split())) for _ in range(q)]
    answer = ''
    for i in range(q) :
        for j in range(changes[i][0]-1, changes[i][1]) : boxes[j] = i+1
    for box in boxes :
        answer += ' ' + str(box)
    print("#{0}{1}".format(case, answer))