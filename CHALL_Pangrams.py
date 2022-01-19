#   Problem Statement
#
#   A word or a sentence is called a pangram if all 
#   the characters of this language appear in it at
#   least once, either in lowercase or in uppercase.
#   You are given a string S consisting of lowercase
#   and uppercase English letters. If the string is
#   a pangram, print "YES" else print "NO", 
#   without the double quotes.
#   
#   Input
#   A single string S.
#   
#   Output
#   Print "YES", if the string is a pangram, else print "NO".
#   
#   Constraints
#   1 ≤ S.length ≤ 100
#   
#   Sample Input
#   QuickWaftingZephyrsVexBoldJim
#   
#   Sample Output
#   
#   YES
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#python 3.7.1

import string
  
alphabet = set(string.ascii_lowercase)
  
def ispangram(string):
    return set(string.lower()) >= alphabet
      
# Driver code
string = input()
if(ispangram(string) == True):
    print("YES")
else:
    print("NO")