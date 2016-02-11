#Cray Jaeger
#CAJ2585

#Prompt user to input the days they want to plan for
days = input('How many days would you like to plan for? ')
info = []
for i in range(0,days,1):
    #for all the days, add the info
    info.append( raw_input('Enter major event for day ' + str(i+1) + ': '))
day = -1
#find out what day they want to hear about
while (day != 0):
    day = input('What day would you like to hear about? Enter 0 to quit: ')
    if (day != 0):
        #print out the info
        print 'On day', day, ':', info[day-1]
    else:
        print 'Bye!'
        
    
