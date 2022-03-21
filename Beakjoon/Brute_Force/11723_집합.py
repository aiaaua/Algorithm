S = list()
for i in range(int(input())) :
    comm = list(input().split())
    if comm[0] == "add" : S.append(int(comm[1]))
    elif comm[0] == "remove" : S.remove(int(comm[1]))
    elif comm[0] == "check" : print(1) if int(comm[1]) in S else print(0)
    elif comm[0] == "toggle" : S.append(int(comm[1])) if int(comm[1]) not in S else S.remove(int(comm[1]))
    elif comm[0] == "all" : S = [i for i in range(1, 21)]
    elif comm[0] == "empty" : S.clear()
