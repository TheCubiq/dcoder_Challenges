#   Problem Statement
#
#   As the students were not focusing much on the lecture.
#   The professor became very angry and decided to give a
#   homework to all the students. So some of the students
#   started trying to convince the professor not to do so.
#   So the professor gives them a K digits and asks the
#   students to make the largest number possible from these
#   digits. If they able to do it, they don't need to do the
#   homework. So you being the smartest student decided to
#   solve the problem.
#   
#   Input
#   The first line of input consists of single integer T denoting the number of test cases. The first line of each test case has a single integer K. The second line of each test case consists of K space separated integers denoting K digits.
#   
#   Output
#   Print the largest number possible using these digits.
#   
#   Constraints
#   1<=T<=100. 1<=K<=100. 0<=Digits<=9.
#   
#   Sample Input
#   1
#   5
#   1 4 5 9 2
#   
#   Sample Output
#   
#   95421
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#python 3.7.1

#print ("Hello, Dcoder!")


def findMaxNum(arr,n) :
    # sort the given array in
    # descending order
    arr.sort(reverse = True) 
    # initialize num with starting
    # element of an arr
    num = arr[0]
    # generate the number
    for i in range(1,n) :
        num = num * 10 + arr[i]
    return num
 
# Driver code
if __name__ == "__main__" :
    t = int(input())
    for i in range(t):
        k = int(input())
        arr = list(map(int,input().split()))
        print(findMaxNum(arr,k))
    