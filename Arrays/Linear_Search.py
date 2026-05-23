"""
Problem: Linear Search
Difficulty: Easy
Topic: Arrays

Approach:
- Traverse the array from start to end
- Compare each element with the target
- If target is found, return its index
- If traversal completes and target is not found, return -1

Time Complexity: O(n)
Space Complexity: O(1)

Note:
- Linear Search works on both sorted and unsorted arrays
"""
def ls(arr,traget):
    for i in range(len(arr)-1):
        if arr[i] == target:
            return i
    return -1
arr = list(map(int,input("Enter the array:" ).split()))
target = int(input("Enter the target: "))

result = ls(arr,target)
if result != -1:
    print("Target found at index",result)
else:
    print("Not Found")