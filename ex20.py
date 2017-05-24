from sys import argv

script, input_file = argv
# imports script and input file for argv
def print_all(f):
    print f.read()
#The f in print_all stands for the file and the function
# asks to print the contents of the file '''
def rewind(f):
    f.seek(0)
# The seek() function deals with bytes and moves the file
# to the specific byte using the parenthesis. seek(0) moves the file to the
# def print_a_line(line_count, f):
def print_a_line(line_count, f):
    print line_count, f.readline()
# reads the 
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
