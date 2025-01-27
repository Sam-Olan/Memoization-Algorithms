def cutrod(p, n):
    if n == 0:
        return 0
    q = -float('inf')
    
    for i in range(1, n+1):
        q = max(q, p[i] + cutrod(p, n-i))
        
    return q

def cutrodMemo(p, n, memo):
    if memo[n] != -1:
        return memo[n]

    if n == 0:
        memo[n] = 0
        return memo[n]
        
    q = -float('inf')
    for i in range(1, n+1):
        q = max(q, p[i] + cutrodMemo(p, n-i, memo))
        
    memo[n] = q
    return q    

def extendedButrodBottomUp(p, n):
    r = [0] * (n+1)
    s = [0] * (n+1)
    
    for j in range(1, n+1):
        q = -float('inf')
        for i in range(1, j+1):
            if q < p[i] + r[j-i]:
                q = p[i] + r[j-i]
                s[j] = i
        r[j] = q
    return r, s
    
def callFunction(p, n, f):
    if f == "a":
        print(cutrod(p, n)) 
    elif f == "b":
        print(cutrodMemo(p, n, [-1] * (n+1))) 
    elif f == "c":
        r, s = extendedButrodBottomUp(p, n)
        print("The max revenue is", r[n], "the optimal cut sizes are: ")
        while n > 0: # Loop until the rod length reaches 1, i.e. no more cuts can be made
            print(s[n])  
            n -= s[n] # Decrement the rod length by the current piece length    
    else:
        print("Invalid function")



def main():
    p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 35, 38, 42, 46, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
    n = int(input("Enter the length of the rod: "))

    print("Press respective character for function. Function List: \na for cutrod\nb for cutrodMemo\nc for extendedButrodBottomUp")

    f = input("Enter character for the function to use: ")

    callFunction(p, n, f)


if __name__ == "__main__":
    main()  