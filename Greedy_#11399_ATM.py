a = int(input())
b = list(map(int,input().split()))
b.sort()

waiting = 0

for i in range(a) :
    waiting += b[i] * (a-i)
    
print (waiting)
