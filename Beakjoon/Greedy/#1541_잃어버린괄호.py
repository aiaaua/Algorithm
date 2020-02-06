num = input().split("-")
L = []
for a in num : 
    b = a.split("+")
    sum1 = 0
    for c in b : 
        sum1 += int(c)
    L.append(sum1)
    
sum2 = 0
for i in range(1, len(L)) :
    sum2 += L[i]
    
print(L[0] - sum2)
