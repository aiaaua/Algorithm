target = int(input())
s_num = 2
count = 1

while target > count :
    count += s_num; s_num += 1

if s_num%2 == 0 : x = 1 + count - target
else : x = s_num - 1 - (count - target)
    
print(x, "/", s_num-x, sep = "")
