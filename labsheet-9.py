def solve():
    N = int(input("Enter N: "))
    A = []
    for _ in range(N):
        A.append(int(input("Enter element: ")))
 
    for i in range(1, N):
        if A[i] != A[0]:
            return -1

    return abs(A[0])

T = int(input("Enter number of test cases:"))

for _ in range(T):
    print("Result:", solve())