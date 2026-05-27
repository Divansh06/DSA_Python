"""
Problem: Reverse Array
Difficulty: Easy
Topic: Arrays

Approach: Two Pointer (In-place)

- left = 0, right = n-1
- Swap elements
- Move pointers toward center
- Stop when left >= right

Time Complexity: O(n)
Space Complexity: O(1)
"""

def reverse(arr):

    left = 0
    right = len(arr) - 1

    while left < right:

        # swapping
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp

        left += 1
        right -= 1


arr = list(map(int, input("Enter array elements: ").split()))

print("Before:", arr)

reverse(arr)

print("After:", arr)