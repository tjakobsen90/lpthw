def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b
    
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b
    
def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b
    
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b
    
       
print "Let's do some math with the functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
#PEMDAS wordt niet na geleefd, de volgorde van de functions in de functions wordt na geleefd. Beginnend met de meest rechter. Inside-out
# 35 + 74 - 180 * 50 / 2 --> 35 + 74 - 180 * 25 --> 35 + 74 - 4500 --> 35 + -4426 --> 4391

print "That becomes: ", what, "Can you do it by hand?"
