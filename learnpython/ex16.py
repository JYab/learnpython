from sys import argv
# This is where the argument is imported
script, filename = argv
# The user writes down the filename in the terminal here
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
# This is just text to put more detail to the file
raw_input("?")
# This acts as a fake confirmation for deleting a file
print "Opening the file..."
target = open(filename, 'w')
# target var is opening the filename
print "Truncating the file. Goodbye!"
target.truncate()
# target.truncate deletes the file contents
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
# The user adds content to the 3 line variables
print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# Here the target var is adding content to the chosen file witht he filename
print "And finally, we close it."
target.close()
# The target var closes the file
