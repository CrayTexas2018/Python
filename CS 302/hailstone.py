#Cray Jaeger
#CAJ2585

#Init variables
number = int(raw_input('Enter a number greater than 0: '))
count = 0

#Keep repeating our logic until the number is = 1
while (number != 1):
    #If the number is even, / 2
    if (number % 2 == 0):
        print str(number) + ' is even, so I take half: ' + str(number/2) 
        number /= 2
    #If Odd /3 * 2
    else:
        print str(number) + ' is odd, so I take 3n + 1: ' + str((number * 3) + 1) 
        number *= 3
        number += 1
    count += 1
print 'The process took ' + str(count) + ' steps to reach 1'
