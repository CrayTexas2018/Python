#CRAY JAEGER
#CAJ2585

scores = []

#Function that gets the lowest score
def getLowestScore(scores):
    minimum = scores[0]
    #Check every score to see if the next score in the array is lower
    for i in scores:
        if i < minimum:
            minimum = i
    #Returns the minimum score
    return minimum

#Function that gets the max score out of an array
def getMaxScore(scores):
    maximum = scores[0]
    #Check every score to see if the next scoe in the array is larger
    for i in scores:
        if i > maximum:
            maximum = i
    #Return the max score
    return maximum

#Function that gets the average score of the judges
def getAverageScore(scores):
    average = 0.0
    #Add the value of every score together
    for i in scores:
        average += i
    #Remove the value of the hiest and lowest scores, and then take the average
    average -= getLowestScore(scores)
    average -= getMaxScore(scores)
    average = average / 5

    #Return the average
    return average 

for i in range(0,7,1):
    #Promp user to input the scores of the judges
    score = input('Enter the score of judge ' + str(i+1) + ':')
    while float(score) < 0 or float(score) > 10:
        score = input('Enter a number between 0 and 10. Your previous number was invalid' + ':')
                  
    scores.append(score)
print 'The average score after discarding the highest score of', str(getMaxScore(scores)), 'and the lowest score of', getLowestScore(scores), 'is:' ,getAverageScore(scores)


        
