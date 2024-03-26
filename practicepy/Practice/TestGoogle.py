# def count_groups(numbers):
#     numbers = sorted(numbers)
#     count = 0
#     consecutive_count = 1
#
#     for i in range(1, len(numbers)):
#         if numbers[i] == numbers[i - 1] + 1:
#             consecutive_count += 1
#         else:
#             count += 1
#             consecutive_count = 1
#
#     if consecutive_count > 0:
#         count += 1
#
#     return count
#
#
# numbers = {18, 1, 3, 7, 11, 12}


def count_groups1(numbers1):
    count = 0
    remaining_numbers = set(numbers1)

    while remaining_numbers:
        current_number = min(remaining_numbers)
        consecutive_group = {current_number}
        while current_number + 1 in remaining_numbers:
            current_number += 1
            consecutive_group.add(current_number)
        remaining_numbers -= consecutive_group
        count += 1

    return count

def count_group1(nums):
    j=1;
    i=0
    count=0;
    while j <= len(nums):
        if (nums[j]-nums[i]) !=1:
            i=j
            j+=1
            count+=1
        else:
            j+=1
            i+=1

    return count


def count_group(nums):
    if not nums:
        return 0

    count = 1  # Initialize count to 1 since we count the first group

    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] != 1:
            count += 1

    return count





numbers1 = [3,1,2,3,6,9,10,11,13]
    #{18, 1, 21, 31, 7, 11, 12}
groups_count = count_group(numbers1)
print("Number of groups possible for consecutive numbers:", groups_count)








