#Cray Jaeger
#CAJ2585

#Init Variables
amount = int(raw_input('Enter a whole number of cents (from 1 to 99). I will output the number of coins that equal the amount: '))
originalAmount = amount

#Find The number of each type of change
quarters = amount / 25
print quarters
#Set the amount left remaining = to whatever we had before
#minus the value of the change we are giving
amount = amount - (25 * quarters)
dimes = int(amount) / 10
amount = amount - (10 * dimes)
nickles = int(amount) / 5
amount = amount - (5 * nickles)
pennies = amount

#Speak English: Check to see if there is <1, 1, >1 of each type of change
#and output the result to sound correct
if (amount > 1):
    output = 'The change for ' + str(originalAmount) + ' cents is: \n'
else:
    output = 'The change for ' + str(originalAmount) + ' cent is: \n'

if (quarters > 1):
    output = output + str(quarters) + ' Quarters '
elif (quarters == 1):
    output = output + str(quarters) + ' Quarter '

if (dimes > 1):
    output = output + str(dimes) + ' Dimes '
elif (dimes == 1):
    output = output + str(dimes) + ' Dime '

if (nickles > 1):
    output = output + str(nickles) + ' Nickles '
elif (nickles == 1):
    output = output + str(nickles) + ' nickle '

if (pennies > 1):
    output = output + str(pennies) + ' pennies '
elif (pennies == 1):
    output = output + str(pennies) + ' penny '

    
print output

#print 'The change for ' + str(originalAmount) + ' cents is:'
#print str(quarters) + ' Quarters ' + str(dimes) + ' dimes ' + str(nickles) + ' Nickles ' + str(pennies) + ' Pennies '
