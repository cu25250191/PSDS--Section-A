
def solve():
    t = int(input("Test Cases:"))
    for _ in range(t):
        s = input("Enter a string:").strip()
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        ans = sum(x // 2 for x in freq)
        print("Output",ans)

solve()
