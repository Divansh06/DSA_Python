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