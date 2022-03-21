case = [1, 2]
for i in range(2, 1001) : case.append(case[i-2] + case[i-1])
print(case[int(input())-1]%10007)
