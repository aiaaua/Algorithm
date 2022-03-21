a = input()
nums = list(a)

def find30(nums) :
    sum = 0
    for i in range(len(nums)) :
        nums[i] = int(nums[i])
    for i in range(len(nums)) : 
        sum += nums[i]
    if nums.count(0) !=0 and sum%3 == 0 :
        nums.sort(reverse = True)
        return ''.join(str(n) for n in nums)
    else : 
        return -1
answer = find30(nums)
print(answer)
