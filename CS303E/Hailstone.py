#  File: Hailstone.py

#  Description: Computes longest cycle length for a given range

#  Student Name: Cray Jaeger

#  Student UT EID: CAJ2585

#  Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: 2/7/2016

#  Date Last Modified: 2/10/2016

def main():
    #promp user to enter starting and ending number of range
    startNum = eval (input("Enter starting number of the range: "))
    endNum = eval (input("\nEnter ending number of the range: "))

    # Check user input, if either of the numbers doesn't work, ask for both again
    while startNum < 0 or endNum < 0:
        startNum = eval (input("\nEnter starting number of the range: "))
        endNum = eval (input("\nEnter ending number of the range: "))
 
    while startNum > endNum:
        startNum = eval (input("\nEnter starting number of the range: "))
        endNum = eval (input("\nEnter ending number of the range: "))

    count = 0

    maxNumber = 0
    maxCount = 0


    #For each number in the range, cycle through and see which one has the highest cycle length
    for i in range (startNum, endNum + 1):
        #print (i)
        testNum = i
        count = 0
        #Run the hailstone sequence until it equals 1
        while testNum != 1:
  #          testNum = changeNumber(testNum)
            if testNum % 2 == 0:
                testNum = testNum // 2
            else:
                testNum = 3 * testNum + 1
            count = count + 1
            if count > maxCount:
                maxCount = count
                maxNumber = i

    #output the results
    #print(maxCount, maxNumber)
    print("\nThe number " + str(maxNumber) + " has the longest cycle length of "+ str(maxCount) + ".")
         

main()
