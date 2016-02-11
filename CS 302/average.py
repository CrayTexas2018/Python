numStudents = input('Enter Number of Students ')
i = 0
nameList = []
gradeList = []

while (i < numStudents):
    name = raw_input('Enter Students Name ')
    nameList.append(name)
    gradeList.append(input('Enter Student Grade: '))
    i += 1
                     
searchName = raw_input('Enter name of student you are looking for: ')
count = 0
found = False
for i in nameList:
    if (i == searchName):
            print gradeList[count]
            found = True
    count += 1
if (found == False):
    print 'Sorry name not found'
