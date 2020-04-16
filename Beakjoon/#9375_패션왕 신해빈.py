for _ in range(int(input())) :
    item_list = dict()
    result = 1
    for i in range(int(input())) : 
        n, t = input().split()
        if t in item_list.keys() : item_list[t].append(n)
        else : item_list[t] = [n]
    for key in item_list.keys() : result = result * (len(item_list[key]) + 1)
    print(result-1)
