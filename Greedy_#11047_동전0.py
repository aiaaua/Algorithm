a, b = map(int, input().split())
coins = list(int(input()) for _ in range(a))

coin_num = 0

for i in range(1, a+1) :
    coin = coins[-i]
    if b >= coin :
        num = b//coin
        b -= coin*num
        coin_num += num

print(coin_num)
