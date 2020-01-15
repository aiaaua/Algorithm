case_num = int(input())
number = [int(input())-1 for _ in range(case_num)]
max_num = max(number) - 10

P = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

if max_num > 0 :
    for i in range(max_num+1) :
        P.append(P[9+i] + P[5+i])

for i in number :
    print(P[i])

