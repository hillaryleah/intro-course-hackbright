# Mid-Session: Dictionary 

# 1) Dictionary of Letters: This dictionary will count the number of times a letter appears in a file and create
	# a dictionary which stores the letters as keys and the letter count as the values. 
		# The code needed to upload and store the file has been commented out. 

# with open ("one_fish.txt") as one_fish: # opens file 
	#one_fish = one_fish.readlines() # saves file as a list, in which each line is an item on a single list  

def letter_count(file):
	import re
	file = ' ,'.join(file) # convert file, which is made of lists, into a string
	file = file.upper() # convert all strings to upper case to obtain accurate count for letters
	file = re.sub("[^\w-]", "", file) # remove special characters from file
	letter_count = {} # create empty dictionary to hold letters and letter count
	for letter in file: # for all letters in the file 
		if (letter not in letter_count): # if letter is not in the dictionary
			letter_count[letter] = 1 # add letter to dictionary with value of 1
		else: # if letter already in the dictionary
			letter_count[letter] +=1 # update the value of the key by adding 1 
	return letter_count	

print letter_count(one_fish)	


# 1) Dictionary of Letters: This dictionary will count the number of times a word appears in a file and create
	# a dictionary which stores the words as keys and the word count as the values. 
		# The code needed to upload and store the file has been commented out. 

# with open ("steve.txt") as steve: # open file 
# 	steve = steve.readlines() # saves file as a list, in which each line is an item on a single list  

def word_count(file):
	import re
	file = ' ,'.join(file) # convert file, which is made of lists, into a string
	file = file.upper() # convert all strings to upper case to obtain accurate count for words
	file = re.sub("[^\w-]", " ", file) # remove special characters
	file = file.split(" ") # split string into individual words and add each word to an index in a list 
	letter_count = {} # create empty dictionary to hold characters
	letter = 0
	for letter in file: # for all indexes in the file 
		if (letter not in letter_count): # if word is not in the dictionary
			letter_count[letter] = 1 # add word to dictionary with value of 1
		else: # if word already in the dictionary
			letter_count[letter] +=1 # update the value of the key by adding 1 
	return letter_count	

print word_count(steve)	

#To do: Need to remove '' from dictionary, could not figure out how to do this. 



	 				
