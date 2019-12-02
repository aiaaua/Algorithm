a = int(input())
rope = []
for _ in range(a) :
    rope.append(int(input()))
rope.sort(reverse = True)

answer = 0
for i in range(a): 
    if answer < rope[i]*(i+1) : 
        answer = rope[i]*(i+1)
print(answer)
