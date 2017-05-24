# this one is like your scripts with argv
def print_two(*args):
# line2 defines the print2 function
    arg1, arg2 = args
# defines what arguements go into args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
# prints the two arg variabls and shows what strings are put into the variables
#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
'''     gives the print2again var the two args directly into its parenthesis and
prints out the strings from arg1,2 just like line6.

'''
# thsi just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin',"


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
''' These line adds what each arg variable will have
In this case, arg1 = Zed & arg2 = Shaw'''
print_one("First!")
# Since print1 only has one argument, there is only one string to put into it
print_none()
# print_none doesn't have any strings so it doesn't print anything
