# Initialize variables
sum = 0.0
count = 0

# Get the input from the user
newNum = input("Enter a number, or 0 to quit: ")
while newNum != 0:
	sum = sum + newNum
	# The same as:
	# count = count + 1
	count += 1
	
	newNum = input("Enter a number, or 0 to quit: ")

if count == 0:
	print "Error: no numbers"
else:
	print "The average of your numbers is", sum/count
