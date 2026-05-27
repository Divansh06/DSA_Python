"""
Problem: Two Sum
Approach 3: HashMap - OPTIMAL

Time Complexity: O(n)
Space Complexity: O(n)

Key Idea:
- complement for each element = target - arr[i]
- if complement is already present,
  then answer is found
"""

def twosum(arr, target):

    hashmap = {}

    for i in range(len(arr)):

        complement = target - arr[i]

        # if complement already exists
        if complement in hashmap:

            return hashmap[complement], i

        # store current element with index
        hashmap[arr[i]] = i

    return -1, -1


n = int(input("Enter the size of array: "))

arr = list(map(int, input("Enter the elements of array: ").split()))

target = int(input("Enter the target: "))

result = twosum(arr, target)

print("The indices are:", result)