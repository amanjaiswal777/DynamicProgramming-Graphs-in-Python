def countSquares(matrix):
    result = 0
    # creating a m * n size matrix with 0 values as default
    dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    # Iterate through the whole matrix

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == 0 or j == 0:
              dp[i][j] = matrix[i][j]
            elif matrix[i][j] == 1:
              dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]) + 1
            else:
              dp[i][j] = 0

    for item in dp:
        for l in range(len(dp[0])):
            result += item[l]

    return result

if __name__ == "__main__":
    matrix = [
    [1,1,0,1],
    [1,0,1,1],
    [1,1,1,1],
    [1,1,1,1]
    ]
    print(countSquares(matrix))