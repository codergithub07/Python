def min_xor_after_removal(arr):
    
    XOR = arr[0]
    
    temp = []
    
    temp = arr.copy()
    
    nXOR = temp[0]

    # Calculate XOR of adjacent pairs
    for i in range(1, N):
        XOR = XOR ^ arr[i]

    if XOR == 0:
        return 0
    
    else:
        
        for i in range(0, N):
            temp = temp.remove(temp[i])
            for j in range(0, N-i-1):
                nXOR = nXOR ^ temp[j]
            nArray.append(nXOR)
        
        minValueIndex = nArray.index(min(nArray))
        
        arr = arr.remove(minValueIndex)
        
        for i in range(1, N):
            XOR = XOR ^ arr[i]
        
        return XOR
  
  
# Input the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Input the number of elements in the array
    N = int(input())
    
    # Input the array elements
    arr = list(map(int, input().split()))

    # Find and print the final minimum XOR after removing at most one element
    result = min_xor_after_removal(arr)
    print(result)
