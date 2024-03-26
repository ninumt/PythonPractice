def findHighestSum(arr, k):
    arr.sort()
    maxSum, minSum=0,0
    for i in arr[:k]:
        minSum+=i
    for j in arr[-k:]:
        maxSum += j
    print(type(minSum))
    return minSum, maxSum

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    maxSum=sum(arr[-3:])
    minSum=sum(arr[:3])
    return minSum, maxSum

arr=[2,1,4,5,3]
print(miniMaxSum(arr))#10,14
print(findHighestSum(arr,3))
