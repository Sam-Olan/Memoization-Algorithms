def CUTRODWITHCOST(p, n, c):
    r = [0] * (n + 1) # r[j] stores the maximum revenue for a rod of length j   
    s = [0] * (n + 1) # s[j] stores the size of the first piece to cut off

    for j in range(1, n + 1): # Check each potential length of rod
        q = -float('inf') 
        for i in range(1, j + 1): # Check each potential cut size
            current_revenue = p[i] + r[j - i] - (c if j != i else 0)
            if q < current_revenue:
                q = current_revenue
                s[j] = i  # Update the optimal cut size for length j
        r[j] = q  # Store the maximum revenue for length j
    return r, s

def PrintCutRodWithCost(p, n, c):
    # r is an array of max revenues per rod length
    # s is an array of optimal cut sizes per rod length 
    r, s = CUTRODWITHCOST(p, n, c) #Get the values for r and s

    print("The max revenue is", r[n], "\nOptimal sizes are:")
    while n > 0: # Loop until the rod length reaches 1, i.e. no more cuts can be made
        print(s[n])  
        n -= s[n] # Decrement the rod length by the current piece length    
    return
    
def main():
    p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30] #Sell price for rod lengths (lenth i)
    
    while True:
        try:
            n = int(input("Enter the length of the rod you want to cut: "))
            if n < 0:
                print("Please enter a positive number")
                continue
            if n >= len(p):
                print(f"Please enter a number less than {len(p)}")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number")
    
    c = 1 # Cost per cut
    PrintCutRodWithCost(p, n, c)
    print("--------------------------------")

if __name__ == "__main__":
    main()