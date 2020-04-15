a, b = map(int, input().split())

if a > b : large, small  = a, b
else : large, small = b, a

while small != 0 :
    large = large%small
    large, small = small, large

print(large)
print(int(a*b/large))
