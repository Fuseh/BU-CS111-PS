print("*************************************************************************")
pi = [3, 1, 4, 1, 5, 9]
e = [2, 7, 1]

print("Problem 1: Indexing and slicing puzzles")
print()
#Puzzle 0: print 2,5,9
answer0 = e[:1], pi[4:]
print("0:",answer0)

#Puzzle 1: print 2, 7
answer1 = e[:2]
print("1:",answer1)

#Puzzle 2: print 5, 4, 3
answer2 = pi[4],pi[2],pi[0]
print("2:",answer2)

#Puzzle 3: print 3, 5, 7
answer3 = pi[0],pi[4],e[1:2]
print("3:",answer3)

#Puzzle 4: print 1, 2, 3, 4, 5
answer4 = e[:3],e[0:1],
print("4:",answer4)

print()
print("Problem 1: Part 2 w/ b.u.t")
b = 'boston'
u = 'university'
t = 'terriers'

#Puzzle 5: print 'bossy'
answer5 = b[:3]+u[-4]+u[-1]
print("5:",answer5)

#Puzzle 6: print 'universe'
answer6 = u[:7]+t[1]
print("6:",answer6)

#Puzzle 7: print 'roster'
answer7 = t[-2]+b[1:4]+t[1:3]
print("7:",answer7)

#Puzzle 8: print 'boisterous'
answer8 = b[:2]+u[7:5:-1]+t[:3]+b[1]+u[0]+b[2]
print("8:",answer8)

#Puzzle 9: print 'yesyesyes' + BONUS: best is 4ops.
answer9semi = u[-1]+t[1]+t[-1]
answer9 = answer9semi * 3
print("9:",answer9)

#Puzzle 10: print 'trist'
answer10 = t[0]+t[3:5]+t[-1]+u[-2]
print("10:",answer10)

print()
print()
print("Problem 2: Understanding statements, program flow and variable scope")
#Puzzle 1: Math Python Program:
x = 11
y = 5
x = x + 6 # x = 17
z = y + x # z = 22
x = x // 7 # x = 2
y = z % 3  # y = 1

print("x:",x) #Correct
print("y:",y) #Correct
print("z:",z) #Correct

print()
print("Problem 2: Part 2 Questions A-F")
#Puzzle 2: Math Python | Parts a-f:
print("A. a += 5")
print("B. b ** a") #Raising a to the power of b
print("C. b = a/3")
print("D. a == b")
print("E. a % 3")
print("F. if b =< 6 or b >= 16: "
      "       outsideRange = True"
      "    :")

print()
print("Problem 2: Part 3 Functions Table + Arithmetic")
def foo(a, b):
    a = a + 2
    b = a - b
    print('foo', a, b)
    return a

a = 7
b = 4
print(a, b)
b = foo(a, b)
print(a, b)
foo(b, a)
print(a, b)

print("""  a  |  b  
-----------
  7  |  4     
     |
        """)

print()
print("Problem 3: Functions with numeric inputs")
#Puzzle 0: Opposite(x)
def opposite(x):
    x *= -1
    return x #This is a NECESSITY in all functions.
print("(OPPOSITE) TestRun 1:", opposite(5))
print("(OPPOSITE) TestRun 2:", opposite(-6))
print("(OPPOSITE) TestRun 3:", opposite(0))
print("Summary - All testruns successful. Function works as intended.")

print()
#Puzzle 1: cube(x)
def cube(x):
    x = x ** 3
    return x
print("(CUBE) TestRun 1:", cube(2))
print("(CUBE) TestRun 2:", cube(-5))
print("(CUBE) TestRun 3:", cube(0))
print("Summary - All testruns successful. Function works as intended.")

print()
#Puzzle 2: compare(num1,num2)
def compare(num1, num2):
    if num1 > num2:
        return 1
    elif num2 > num1:
        return -1
    else:
        return 0
print("(COMPARE) TestRun 1:",compare(5, 2))
print("(COMPARE) TestRun 2:",compare(2, 5))
print("(COMPARE) TestRun 3:",compare(2, 2))
print("Summary - All testruns successful. Function works as intended.")

#Puzzle 3: convert_from_inches(inches)

def convert_from_inches(inches):
    yards = 0
    feet = 0
    inches2 = 0
    while inches / 36 >= 1:
        yards += 1
        inches -= 36
    if inches / 36 < 1:
        while inches / 12 >= 1:
            feet += 1
            inches -= 12
    if inches / 12 < 1:
        inches2 = inches
    return yards, feet, inches2
print("(CONVERT) TestRun 1:",convert_from_inches(67))
print("(CONVERT) TestRun 1:",convert_from_inches(75))
print("(CONVERT) TestRun 1:",convert_from_inches(0))
print("Summary - All testruns successful. Function works as intended.")



print()
print("*************************************************************************")