import sys

prime_list = list()
check = [False]*3 + [True]*999998

for i in range(3, 1000001) :
    if check[i] :
        prime_list.append(i)
        for j in range(2*i, 1000000, i) : check[j] = False

while True :
    num = int(sys.stdin.readline().rstrip())
    if num == 0 : break
    for prime in prime_list :
        if check[num-prime] :
            print("{0} = {1} + {2}".format(num, prime, num-prime))
            break
    else : print("Goldbach's conjecture is wrong.")
