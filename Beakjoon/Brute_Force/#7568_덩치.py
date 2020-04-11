n = int(input())
peoples = [list(map(int, input().split())) for i in range(n)]

for people in peoples :
    cnt = 1
    for another in peoples :
        if people[0] < another[0] and people[1] < another[1] : cnt += 1
    print(cnt, end = " ")
