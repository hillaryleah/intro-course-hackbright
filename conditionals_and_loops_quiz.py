# Mid- Session Take Home Quiz: Loops and Conditionals

# 1. Write a function that takes in a number and prints that number of rows and columns of *

# create function with single parameter
def draw_asterisks(num):
	# for every item within the num range
	for i in range(num): 
		# print asterisk(s) on row. num of asterisk(s) = num (argument passed when function called)
		print "*" * num

# call the function, pass the num 8. Function will be intialized 8 times, which 
  # results in 8 rows of 8 asterisks being printed		
draw_asterisks(8)	
print 


# 2 Write a function that draws a checkerboard with x's and o's 

# create function that takes no parameters
def draw_checkboard():
	# setting the range as 8 since there are 8 rows for the checkboard
	  # so function needs to fun 8 times 
	for i in range(8): 
		# print variation1 on even numbered rows
		if i % 2 == 0: 
			print "x o x o x o x o"
		# print variation2 on off numbered rows
		else: 
			print "o x o x o x o x"	

# call the function 
draw_checkboard()

