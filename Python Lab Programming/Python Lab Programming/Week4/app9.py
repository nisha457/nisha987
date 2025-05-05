def printTheArray(arr, n): 
    for i in range(n): 
        print(arr[i], end=" ") 
    print()

# Function to generate all binary strings 
def generateAllBinaryStrings(n, arr, i): 
    if i == n: 
        printTheArray(arr, n) 
        return
    
    arr[i] = 0 
    generateAllBinaryStrings(n, arr, i + 1) 

    arr[i] = 1 
    generateAllBinaryStrings(n, arr, i + 1) 

# Driver Code 
if __name__ == "__main__": 
    n = 4
    arr = [None] * n 
    generateAllBinaryStrings(n, arr, 0)
