"""
 * Problem: Two Sum
 * Approach 1: Brute Force
 * Time complexity : O(n²) | Space complexity: O(1)
"""
def twosum(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == target:
                return i,j
    return -1,-1 # if target not found

arr = list(map(int,input("Enter the elements :").split()))
target = int(input("Enter the target :"))

result = twosum(arr,target)
print("The indices are :",result)