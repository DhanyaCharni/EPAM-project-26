N = int(input())

points = list(map(int, input().split()))

if N == 1:
    print(points[0])
else:

    dp = [0] * N

    dp[0] = points[0]
    dp[1] = max(points[0], points[1])

    for i in range(2, N):
        dp[i] = max(dp[i - 1], dp[i - 2] + points[i])

    print(dp[N - 1])
