from sys import argv
# This is importing the argument the user has to write out
script, filename = argv
# script and filename are the 2 variables needed to write out in the terminal
txt = open(filename)
# The txt is opening the filename given by the user
print "Here's your file %r:" % filename
# Here is where the filename is put in a string
print txt.read()
# The file is read and is writen at this point
print "Type the filename again:"
file_again = raw_input(">")
# Here it is asking for the filename again using a new variable
txt_again = open(file_again)
# Another new variable is opening the file_again
print txt_again.read()
# Here it prints the ex15_sample.txt contents
txt_again.close()
#This closes the file object which is necessary
