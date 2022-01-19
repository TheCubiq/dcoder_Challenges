#   Problem Statement
#   All numbers in NumberLand are standing in a circle for a dancing ceremony. 
#   Every number needs a dancing partner. 
#   Dancing partner of any number is the number which is 
#   standing radially opposite to it in the circle. 
#   The numbers are from 0 to N-1. 
#   A certain number X wants to know who will be its dancing partner. 
#   Please help X.
#   
#   Input
#   Two positive integers denoting the value of N and X.
#   
#   Output
#   Print the number radially opposite to X in a circle of N numbers.
#   
#   Constraints
#   4 ≤ N ≤ 20 0 ≤ X < N
#   
#   Sample Input
#   8 2
#   
#   Sample Output
#   
#   6
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#python 3.7.1

n,x = list(map(int, input().split()))
a= (n/2)
b= (x+a)%n
print(int(b))