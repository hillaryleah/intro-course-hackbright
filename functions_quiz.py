# Mid- Session Take Home Quiz: Functions 

# 1. Function that takes three arguments(hours, minutes, seconds) and returns total in seconds
def convert_to_seconds(hours, minutes, seconds): 
	# get total minutes by converting hours to minutes and adding minutes 
	total_minutes = (hours *60) + minutes
	# get total seconds my converting total minutes to seconds and adding seconds 
	total_seconds = (total_minutes * 60) + seconds
	# return the total seconds 
	return total_seconds

print convert_to_seconds(1.6,2,1.666)

# 2. Function that takes 2 parameters (feet, inches) and returns total in inches
def convert_to_inches(feet, inches):
	# get total inches by converting feet to inches and adding to inches
	total_inches = (feet * 12) + inches
	# return total in inches
	return total_inches

print convert_to_inches(0,7)	

	