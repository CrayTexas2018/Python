
#  File: Day.py

#  Description: Print out day of week for any given date between 1900 and 2100

#  Student Name:Cray Jaeger

#  Student UT EID: CAJ2585

#  Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: 2/1/2016

#  Date Last Modified: 2/6/2016

def main():
    # Initialize variables, set them negative so while loop works
    year = -10
    a = -10
    b = -10

    # Prompt user to enter year
    while year < 1900 or year > 2100:
        year = eval(input("Enter year: "))

    # Prompt user to enter month
    while a < 1 or a > 12:
        a = eval(input("Enter month: "))

    # Check to see how many days are in the given month
    numDays = -10
    isLeap = False
    if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
        numDays = 31
    elif a == 4 or a == 6 or a == 9 or a == 11:
        numDays = 30
    else:
        # Check Leap Year
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            isLeap = True
            numDays = 29
        else:
            isLeap = False
            numDays = 28
            
    if (a == 1):
        a = 11
        year = year - 1
    elif (a == 2):
        a = 12
        year = year - 1
    else:
        a = a - 2

    # Prompt user to enter the day
    while (b < 1 or b > numDays):
        b = eval(input("Enter day: "))


    # Calculate what day of the week it is according to forumla
    c = year%100 - 0
    d = year//100

    w = (13 * a - 1 ) // 5 

    x = c // 4 

    y = d // 4 

    z = w + x + y + b + c - 2 * d 

    r = z % 7 

    r = (r + 7) % 7
    
    day = ""
    if (r == 0):
        day = "Sunday"
    elif (r == 1):
        day = "Monday"
    elif (r == 2):
        day = "Tuesday"
    elif (r == 3):
        day = "Wednesday"
    elif (r == 4):
        day = "Thursday"
    elif (r == 5):
        day = "Friday"
    elif (r == 6):
        day = "Saturday"
    else:
        print ("Error, day out of range!")

    # Print the day
    print()
    print ("The day is", day + ".")
    
main()
