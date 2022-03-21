def count_case(target) :
    if target == 1 : return 1
    if target == 2 : return 2
    if target == 3 : return 4
    return count_case(target-1) + count_case(target-2) + count_case(target-3)

for _ in range(int(input())) :
    target = int(input())
    print(count_case(target))
