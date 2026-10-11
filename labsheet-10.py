def solve():
    n = int(input("Enter n: "))
    nums = list(map(int, input("Enter the numbers: ").split()))

    count = {}

    for num in nums:
        s = sum(map(int, str(num)))
        count[s] = count.get(s, 0) + 1

    ans = 0
    for freq in count.values():
        ans += freq * (freq - 1) // 2

    print("Answer:", ans)
solve()



