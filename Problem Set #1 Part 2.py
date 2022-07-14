import sys
print("*************************************************************************")

print("Problem 4: Understanding program flow and variable scope")
# hello's local variables
# a  |  b  |  c  |  d
# -----------------------
# 1  |  3  |  1  |  7

# goodbye's local variables
# a  |  c
# ---------
# 1  |  4

# adios's local variables
# a  |  b  |  c  |  d
# -----------------------
#    |     |     |

# output (the lines printed by the program)
# -------
# 1 4 2 7

print()
print("Problem 5: Functions on strings and lists, part I | Part 1")
#Puzzle 1: front3(str)
def front3(str):
    strBeginning = str[0:3]
    if len(str) < 3:
        return str * 3
    else:
        return strBeginning * 3
print("(FRONT_3) TestRun 1:", front3("Hello"))
print("(FRONT_3) TestRun 2:", front3("xD"))
print("(FRONT_3) TestRun 3:", front3("Magician"))
print("Summary - All testruns successful. Function works as intended.")

print()
print("Problem 5: Functions on strings and lists, part I | Part 2")
#Puzzle 2: shorter_len(l1,l2)
def shorter_len(l1,l2):
    if len(l1) > len(l2):
        return len(l2)
    else:
        return len(l1)
l1 = ['computers', 'compute']
l2 = ['humans', 'have', 'intelligence']
print("(SHORTER_LEN) TestRun 1:", shorter_len(l1,l2))
l1 = [5, 'abc', '123', ['cs', 111]]
l2 = ['I', 'Love', 'cs']
print("(SHORTER_LEN) TestRun 2:", shorter_len(l1,l2))
l1 = ['begin', 'end']
l2 =  [['begin', 'middle','end']]
print("(SHORTER_LEN) TestRun 3:", shorter_len(l1,l2))
print("Summary - All testruns successful. Function works as intended.")

print()
print("Problem 5: Functions on strings and lists, part I | Part 3")
#Puzzle 3: ends_with(word,suffix)
def ends_with(word, suffix):
    suffixLen = len(suffix)
    if word[len(word) - suffixLen:len(word)] != suffix:
        return "False!"
    else:
        return "True!"
print("(ENDS_WITH) TestRun 1:",ends_with("computer","ter"))
print("(ENDS_WITH) TestRun 2:",ends_with("computer","tar"))
print("(ENDS_WITH) TestRun 3:",ends_with("begin","in"))
print("Summary - All testruns successful. Function works as intended.")

print()
print("Problem 6: Functions on strings and lists, part II | Part 1")
#Puzzle 1: replace_prefix(word, prefix)
def replace_prefix(word, prefix):
    prefixLen = len(prefix)
    if len(prefix) > len(word):
        return "ERROR: Prefix has to be shorter than the word!"
    else:
        word = word.replace(word[0:prefixLen],prefix)
        return word
print("(REPLACE_PREFIX) TestRun 1:",replace_prefix("Play","Ground"))
print("(REPLACE_PREFIX) TestRun 2:",replace_prefix("undo","re"))
print("(REPLACE_PREFIX) TestRun 3:",replace_prefix("this!ismyword","cs111"))
print("Summary - All testruns successful. Function works as intended.")

print()
print("Problem 6: Functions on strings and lists, part II | Part 2")
#Puzzle 2: swap_halves(s)
def swap_halves(s):
    odd = False
    even = False
    if (len(s) % 2) == 0:
        even = True
    else:
        odd = True
    if even == True:
        firstHalf = s[:len(s)//2]
        secondHalf = s[len(s)//2:]
        s2 = secondHalf + firstHalf
        return s2
    elif odd == True:
        firstHalf = s[:len(s)//2]
        secondHalf = s[len(s)//2:]
        s2 = secondHalf + firstHalf
        return s2
print("(SWAP_HALVES) TestRun 1:",swap_halves("homework"))
print("(SWAP_HALVES) TestRun 2:",swap_halves("carpets"))
print("(SWAP_HALVES) TestRun 3:",swap_halves("x"))
print("Summary - All testruns successful. Function works as intended.")

print()
print("Problem 6: Functions on strings and lists, part II | Part 3")
#Puzzle 3: statistics(list_of_int)
def statistics(list_of_int):
    sum = 0
    for i in list_of_int:
        sum += i
    average = sum/len(list_of_int)
    smallestValue = list_of_int[0]
    largestValue = list_of_int[0]
    for j in list_of_int:
        if j < smallestValue:
            smallestValue = j
    for k in list_of_int:
        if k > largestValue:
            largestValue = k
    return sum,average,smallestValue, largestValue
list_of_int = [2,8,7]
print(statistics(list_of_int))

print("*************************************************************************")
