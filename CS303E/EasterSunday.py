
#  File: EasterSunday.py

#  Description: Calculates when Easter Sunday is for any given year

#  Student Name:Cray Jaeger

#  Student UT EID: CAJ2585

#  Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: 2/1/2016

#  Date Last Modified: 2/1/2016

def main():
    # Prompt user to input year
    y = eval (input("Enter year: "))

    # Calculate Easter Sunday based on formula
    a = y % 19
    b = y//100
    c = y % 100
    d = b//4
    e = b%4
    g = (8*b+13)//25
    h = (19*a+b-d-g+15)%30
    j = c//4
    k = c%4
    m = (a+11*h)//319
    r = (2 * e + 2 * j - k - h + m + 32)%7
    n = (h-m+r+90)//25
    p = (h-m+r+n+19)%32

    month = ""
    if n == 3:
        month = "March"
    elif n == 4:
        month = "April"
    else:
        print ("Error, month isn't March or April")

    #Print the results (When Easter Sunday is.")
    print()
    print ("In", y, "Easter Sunday is on", p, month + ".")

main()
