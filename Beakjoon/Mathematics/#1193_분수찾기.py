target = int(input())
i, s = 2, 1
while target > s :
    s += i
    i += 1
a = [s-target+1, i-s+target-1][i%2]
print(a, "/", i-a, sep = '')
