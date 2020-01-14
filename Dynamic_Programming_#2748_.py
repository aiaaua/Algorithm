target = int(input())
f_0, f_1 = 0, 1

for i in range(target-1) :
    f_0, f_1 = f_1, f_0 + f_1

print(f_1)
