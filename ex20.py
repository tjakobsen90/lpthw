from sys import argv

script, input_file = argv

#variables in een script en een function zijn los van elkaar, unieke namen zijn alsnog gewenst
def print_all(f):
    print f.read()
    
def rewind(f):
    f.seek(0)
    
def print_a_line(line_count, f):
    print line_count, f.readline(), # , voorkomt dubbele enter (implict \n aan het einde van print)
    
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
