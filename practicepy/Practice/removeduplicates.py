""""Remove duplicates from sorted or unsorted list"""

def removeDuplicates(nums):
        if not nums:#if len(nums)==0:
            return 0

        i=0
        for j in range(1,len(nums)):
            if(nums[i]!=nums[j]):
                i+=1
                nums[i]=nums[j]

        return i+1


def removeDuplicatesUnsorted(nums):
    if not nums:  # if len(nums)==0:
        return 0

    nums.sort()
    i = 0
    for j in range(1, len(nums)):
        if (nums[i] != nums[j]):
            i += 1
            nums[i] = nums[j]

    return i + 1

nums = [1,2,2,3,4,4,5]
result_len=removeDuplicates(nums=nums)
print(nums[:result_len])

nums = [3,2,5,6,7,1,7,4,4,1]
result_len=removeDuplicatesUnsorted(nums=nums)
print(nums[:result_len])




























"""def removeDuplicates(nums):
    if not nums:  # if len(nums)==0:
        return 0

    i = 0
    print("i : " + str(i))
    for j in range(1, len(nums)):
        print("j before check : " + str(j))
        if (nums[i] != nums[j]):
            print("j : " + str(j))
            i += 1
            print("i : " + str(i))
            nums[i] = nums[j]
            print(f"nums[{i}] : " + str(nums[i]))

    return i + 1"""



