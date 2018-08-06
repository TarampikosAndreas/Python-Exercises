#Solution I found on the Internet

# Python Code to find 
# rank of elements
def rankify(A):
 
    # Rank Vector
    R = [0 for x in range(len(A))]
 
    # Sweep through all elements
    # in A for each element count
    # the number of less than and 
    # equal elements separately
    # in r and s.
    for i in range(len(A)):
        (r, s) = (1, 1)
        for j in range(len(A)):
            if j != i and A[j] < A[i]:
                r += 1
            if j != i and A[j] == A[i]:
                s += 1      
        
        # Use formula to obtain rank
        R[i] = r + (s - 1) / 2
 
    # Return Rank Vector
    return R
 
if __name__ == "__main__":
    A = [10,8,15,12,6,20,1]
    print(A)
    print(rankify(A))
