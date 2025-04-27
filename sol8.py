def solve_pokerogue(T, test_cases):
    results = []
    for t in range(T):
        N, K = test_cases[t][0], test_cases[t][1]
        A = test_cases[t][2]
        B = test_cases[t][3]
        C = test_cases[t][4]
        D = test_cases[t][5]

        dp = [0] * (N + 1)

        for i in range(N - 1, -1, -1):
            singles_score = A[i] / B[i] + dp[i + 1]
            doubles_score = (A[i] + C[i]) / D[i] + dp[i + 1]
            lure_score = 0
            if i + K <= N:
                lure_score = sum((A[j] + C[j]) / D[j] for j in range(i, i + K)) + dp[i + K]
            dp[i] = max(singles_score, doubles_score, lure_score)

        results.append(dp[0])

    return results

T = int(input())
test_cases = []

for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))
    test_cases.append((N, K, A, B, C, D))

results = solve_pokerogue(T, test_cases)

for result in results:
    print(f"{result:.7f}")
