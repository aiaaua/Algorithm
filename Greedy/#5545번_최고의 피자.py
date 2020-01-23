t_num = int(input())
d_price, t_price = map(int, input().split())
d_kcal = int(input())
t_kcal = sorted([int(input()) for _ in range(t_num)], reverse = True)

kcal = d_kcal/d_price

for i in range(1, len(t_kcal)) :
    if kcal < (d_kcal + sum(t_kcal[:i]))/(d_price + t_price*i) :
        kcal = (d_kcal + sum(t_kcal[:i]))/(d_price + t_price*i)

print(int(kcal))