#   Problem Statement
#
#   You are given an array of N length. You have to rotate
#   the array rightwards by K rotations, that is, shift 
#   each element to the right by K positions. 
#   Print the rotated array.
#   
#   Input
#   First line contains N and K. Second line contains N integers denoting the array.
#   
#   Output
#   Print the array after the rotation.
#   
#   Constraints
#   1 <= N, K <= 100000 1 <= Arr[i] <= 10^9
#   
#   Sample Input
#   5 2
#   1 2 3 4 5
#   
#   Sample Output
#   
#   4 5 1 2 3
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def RightRotate(a, n, k):
    # If rotation is greater
    # than size of array
    k = k % n
    for i in range(0, n):
        if(i < k):
            # Printing rightmost
            # kth elements
            print(a[n + i - k], end = " ")
        else:
            # Prints array after
            # 'k' elements
            print(a[i - k], end = " ")
    print("\n")
# Driver code
Arr = []
# input arguments
N,K = list(map(int, input().split()))
# input array
Arr = list(map(int, input().split()))
    
RightRotate(Arr, N, K)