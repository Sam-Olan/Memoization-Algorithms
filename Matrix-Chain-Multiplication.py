def MatrixChainOrder(p, n):
    # initialize the tables to hold the min number of multiplications (m) and the split point (s)
    m = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    s = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # initialize the diagonal to 0
    for i in range(1, n + 1): 
        m[i][i] = 0
    
    for l in range(2, n + 1): # l is the current chain length
        for i in range(1, n - l + 2): # start with 2 matrices, increase until l = n
            j = i + l - 1
            m[i][j] = float('inf')
            
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j]

                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s
    

def PrintOptimalParenthesization(s,i,j):
    if i == j: # when there is only one matrix
        return f"A{i}"
    else:
        left = PrintOptimalParenthesization(s, i, s[i][j]) # from i to k
        right = PrintOptimalParenthesization(s, s[i][j] + 1, j) # from k+1 to j
        return f"({left}{right})"
        

def main():
    #p = [5, 10, 3, 12, 5, 50, 6]
    p = [5, 10, 15, 20]
    n = len(p) - 1 # number of matrices to be multiplied

    m, s = MatrixChainOrder(p, n)
    
    result = PrintOptimalParenthesization(s, 1, n)

    print("Optimal Parenthesization:", result)
    print("Minimum number of multiplications:", m[1][n])

if __name__ == "__main__":
    main()