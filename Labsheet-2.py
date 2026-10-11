
#Linear Search
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

arr = [10, 20, 30, 40, 50]

key = int(input("Enter the element to search: "))

result = linear_search(arr, key)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found.")

#Binanry Search

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = [10, 20, 30, 40, 50]
key = int(input("Enter the element to search: "))

result = binary_search(arr, key)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found.")
