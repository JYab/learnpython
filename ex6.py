x = "There are %d types of people." % 10
# %d is formatting for the number 10
binary = "binary"
do_not = "don't"
# These variables are for practicing formatting
y = "Those who know %s and those who %s." % (binary, do_not)
# ^ Here is to format the above variables into a joke
print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
