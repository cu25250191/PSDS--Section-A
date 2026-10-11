def max_sum(arr, k):
    current = sum(arr[:k])
    maximum = current

    for i in range(k, len(arr)):
        current = current + arr[i] - arr[i-k]
        maximum = max(maximum, current)

    return maximum

n = int(input("Enter N: "))
k = int(input("Enter K: "))
arr = list(map(int, input("Enter array elements: ").split()))
print("Maximum Sum:", max_sum(arr, k))

'''s = input().strip()

last = {}
start = 0
ans = 0

for i in range(len(s)):
    if s[i] in last and last[s[i]] >= start:
        start = last[s[i]] + 1

    last[s[i]] = i
    ans = max(ans, i - start + 1)

print(ans)'''

'''n, m, k = map(int, input().split())

edges = []

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

INF = float('inf')
dp = [INF] * (n + 1)
dp[1] = 0

for _ in range(k):
    new_dp = dp[:]

    for u, v, w in edges:
        if dp[u] != INF:
            new_dp[v] = min(new_dp[v], dp[u] + w)

        if dp[v] != INF:
            new_dp[u] = min(new_dp[u], dp[v] + w)

    dp = new_dp

if dp[n] == INF:
    print(-1)
else:
    print(dp[n])'''