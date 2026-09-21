'''import heapq

def priority_queue(arr):
    heap = []
    for x in arr:
        heapq.heappush(heap, x)

    print("Priority Queue:", end=" ")
    while heap:
        print(heapq.heappop(heap), end=" ")

def heap_sort(arr):
    heap = []
    for x in arr:
        heapq.heappush(heap, x)

    return [heapq.heappop(heap) for i in range(len(heap))]

arr = list(map(int, input("Enter elements: ").split()))

print("Min Heap:", end=" ")
h = arr.copy()
heapq.heapify(h)
print(h)

priority_queue(arr)

print("\nHeap Sort:", heap_sort(arr))'''

def maximize_difference(arr):
    arr.sort()
    n = len(arr)
    ans = [0] * n

    l, r = 0, n - 1

    for i in range(n):
        if i % 2 == 0:
            ans[i] = arr[l]
            l += 1
        else:
            ans[i] = arr[r]
            r -= 1

    total = sum(abs(ans[i] - ans[i - 1]) for i in range(1, n))
    return ans, total


arr = list(map(int, input("Enter array elements: ").split()))

result, total = maximize_difference(arr)

print("Rearranged Array:", result)
print("Maximum Sum:", total)

'''def smallest_subarray(arr, target):
    left = 0
    total = 0
    ans = len(arr) + 1

    for right in range(len(arr)):
        total += arr[right]

        while total > target:
            ans = min(ans, right - left + 1)
            total -= arr[left]
            left += 1

    return -1 if ans == len(arr) + 1 else ans


arr = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter target: "))

print("Smallest Subarray Length:", smallest_subarray(arr, target))'''