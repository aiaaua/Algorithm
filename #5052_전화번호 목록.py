import sys
for i in range(int(input())) :
    call_nums = sorted([str(sys.stdin.readline().strip()) for _ in range(int(input()))])
    for j in range(1, len(call_nums)) :
        if call_nums[j-1] == call_nums[j][:len(call_nums[j-1])] : print('NO'); break
    else : print('YES')