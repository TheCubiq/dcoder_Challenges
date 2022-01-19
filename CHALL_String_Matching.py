#   Problem Statement
#   Cody has a sequence of characters N. He likes a sequence if it contains his favourite sequence as a substring. Given the sequence and his favourite sequence F, check whether the favourite sequence is present in the sequence.
#   
#   Input
#   The first line of input contains a single line T, which represents the number of test cases. Each test case consists of 2 strings separated by space N and F respectively.
#   
#   Output
#   Print "Yes" if the sequence contains the favorite sequence in it, otherwise print "No".
#   
#   Constraints
#   1<=T<=10. 1<=|N|,|F|<=100. All the characters are lowercase alphabets.
#   
#   Sample Input
#   2
#   abcde abc
#   pqrst pr
#   
#   Sample Output
#   
#   Yes
#   No
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#python 3.7.1

#print ("Hello, Dcoder!")


def FindMyFav(N,F):
    s_F = False
    # counts for length of letters of N
    for Index_N in range(len(N)):
        # if the letter from N is the first letter from F
        if (N[Index_N] == F[0]):
            # counts for length of letters of F
            for Index_F in range(len(F)):
                # helper printing the letter comparsition
                #print(g[0][Index_N+Index_F] +":"+ g[1][Index_F])
                # if that letter from N and his neighbors are the same as the neighbors of letter from F
                if (N[Index_N+Index_F] == F[Index_F]):
                    # if the whole favorite string was read
                    if Index_F+1 == len(F): 
                        #print("found on pos:" + str(Index_N+1))
                        return "Yes"
                # if the next letters from N didn't match next letters of F, don't continue the loop
                else: break
    return "No"

def FindMyFav2(N,F):
    #finds = 0
    
    for Index_N in range(len(N)):
        a = N[Index_N:len(F)+Index_N]
        print(a)
        if a == F:
            return True
            #finds += 1
    #if finds > 0:
        #return True #,finds
    return False
            

t = int(input(
    "Number of tests: "
))
for _ in range(t):
    N,F = input(
        "word,fav: "
    ).split()
    print(FindMyFav2(N,F))

