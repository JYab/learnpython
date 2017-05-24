from sys import argv
from os.path import exists
#Importing both the argument and the operating system path
script, from_file, to_file = argv
# asking user for the from and to file
print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
in_file = open(from_file)
# in_file opens the from_file
indata = in_file.read()
# indata is a new var that reads the in_file(from_file)
print "The input file is %d bytes long" % len(indata)
# this len function is being formatted into the syntax
print "Doese the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()
# extra detail for user to confirm to read the indata
out_file = open(to_file, 'w')
out_file.write(indata)
# out_file opens and writes the indata content into the to_file
print "Alright, all done."

out_file.close()
in_file.close()
# Closes the out_file and the in_file 
