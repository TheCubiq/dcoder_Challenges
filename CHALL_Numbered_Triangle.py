#   Problem Statement
#
#   You need to print this pattern upto N. 
#   For N = 4, 
#   1 
#   1 2 
#   1 2 3 
#   1 2 3 4
#   
#   Input
#   A single positive integer N.
#   
#   Output
#   Numbered Triangle upto N. Do not leave trailing whitespaces at the end of each line.
#   
#   Constraints
#   1 ≤ N ≤ 9
#   
#   Sample Input
#   3
#   
#   Sample Output
#   
#   1
#   1 2
#   1 2 3
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#python 3.7.1

n = 5
for i in range(n):
    a=1
    for j in range(1,i+1) :
        a = a * 10 + j+1
    print(a)
print("\n")