"""
Problem: Binary Search(with sorted element taken as input)
Difficulty: Easy
Topic: Arrays

Approach:
- Use two pointers: low and high
- Find the middle element of the array
- Compare target with middle element
- If target is greater, move to right half
- If target is smaller, move to left half
- Repeat until element is found or search space becomes empty

Time Complexity: O(log n)
Space Complexity: O(1)

Note:
- Binary Search works only on sorted arrays
"""
def Bs(arr,target):
    low = 0
    high = len(arr) -1

    while low <= high:
        mid = (low+high)//2

        if arr[mid] == target:
            return mid
        elif arr[mid]<target:
            low = mid+1
        else:
            high = mid-1

    return -1

arr = list(map(int,input("Enter the elements in sorted").split()))
target = int(input("Enter the target :"))

result = Bs(arr,target)

if result != -1:
    print("Element found at index :" , result)
else:
    print("Element not found")
