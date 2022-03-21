import sys

m = int(sys.stdin.readline())
S = set()

for _ in range(m):
    line = sys.stdin.readline().strip().split()
    
    if len(line) == 1:
        if line[0] == 'all':
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    else:
        comm, num = line[0], int(line[1])

        if comm == 'add':
            S.add(num)
        elif comm == 'remove':
            S.discard(num)
        elif comm == 'check':
            if target in S:
                print(1)
            else:
                print(0)
        elif comm == 'toggle':
            if target in S:
                S.discard(num)
            else:
                S.add(num)
