height = sorted([int(input()) for _ in range(9)])
sum_h = sum(height)
a, b = int(), int()
for i in height :
    for j in height :
        if i == j : continue
        if sum_h - i - j == 100 :
            a, b = i, j

height.remove(a)
height.remove(b)

for i in height : print(i)
