n = int(input())

for i in range(n) :
    text = list(input())
    for j in range(len(text)//2) :
        if text[j] != text[-j-1] : print("#{0} {1}".format(i+1, 0)); break
    else : print("#{0} {1}".format(i+1, 1))
