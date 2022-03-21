a = 1000 - int(input())
charge = [500, 100, 50, 10, 5, 1]
count = 0

for i in charge : 
    if a >= i :
        b = a//i
        a = a - i*b
        count += b
        
print(count)
