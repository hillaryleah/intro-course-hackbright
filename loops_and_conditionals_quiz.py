#1 Write a function that takes in a number and prints that number of rows and columns of *

def draw_asterisks(num):
	for i in range(num): 
		print "*" * num
draw_asterisks(1)	

# 2 Write a function that draws a checkerboard with x's and o's 
# A checkerboard is an 8 x 8 alternating grid

def draw_checkboard():
	#setting the range as 8 since there are 8 rows
	for i in range(8): 
		# conditional to print 1 variation of the line on even rows
		if i % 2 == 0: 
			print "x o x o x o x o"
		#print the other variation on odd rows
		else: 
			print "o x o x o x o x"	

draw_checkboard()

