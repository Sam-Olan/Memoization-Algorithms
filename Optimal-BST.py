def optimalBST(p, q, n):
    # Initialize the matrices to hold the expected cost (e), cumulative weights (w), and root structure (root)
    e = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    w = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    root = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # Base cases for e and w when theres no actual node (dummy node)
    for i in range(1, n + 1):
        e[i][i - 1] = q[i - 1]
        w[i][i - 1] = q[i - 1]

    
    for l in range(1, n + 1): 
        for i in range(1, n - l + 2): 
            j = i + l - 1 
            e[i][j] = float('inf')
            w[i][j] = w[i][j - 1] + p[j] + q[j]
            
            for r in range(i, j + 1):
                left_cost = e[i][r - 1] if (r - 1 >= i - 1) else 0 # If the left node exists, use its cost, else 0
                right_cost = e[r + 1][j] if (r + 1 <= j) else 0 # If the right node exists, use its cost, else 0
                t = left_cost + right_cost + w[i][j] # Total cost of subtree

                if t < e[i][j]: # If total cost is less than current cost, update the cost and the root
                    e[i][j] = t
                    root[i][j] = r

    return e, w, root

def main():
    p = [0, 0.04, 0.06, 0.08, 0.02, 0.10, 0.12, 0.14] # Probabilities of keys (successes)
    q = [0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05] # Probabilities of dummy nodes (failures)
    n = len(p) - 1  # n represents number of keys

    e, w, root = optimalBST(p, q, n)
    
    print("cost:", e[1][n])
    print("root:", root)   
    print("weights:", w)
    print("expected cost:", e)

if __name__ == "__main__":
    main()