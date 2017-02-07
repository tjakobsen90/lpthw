# variable x waarin %d de interger 10 is
x = "There are %d types of people." % 10
# variable binary met de string binary
binary = "binary"
# variable do_not met de string don't
do_not = "don't"
# variable y met variables binary en do_not verwerkt erin
y = "Those who know %s and those who %s." % (binary, do_not)

# echo variable x
print x
# echo variable y
print y

# echo een string met de exacte waarde van x
print "I said: %r." % x
# echo een string met de (string)waarde van y
print "I also said: '%s'." % y

# varaible hilarious heeft de waarde FALSE
hilarious = False
# variable met een string en een exacte(real) format character
joke_evaluation = "Isn't that joke so funny?! %r"

# echo variable en plaats variable hilarious in de format character
print joke_evaluation % hilarious

# variable w is een string
w = "This is the left side of..."
# variable e is een string
e = "a string with a right side."

# echo de variable w en e aan elkaar geplakt
print w + e

