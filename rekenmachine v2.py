print "Welkom bij de rekenmachine."
cijfer1 = int(raw_input("> "))

prompt = "> %d " % cijfer1
functie = str(raw_input(prompt))

if functie == "+":
    add = "> %d + " % cijfer1
    cijfer2 = int(raw_input(add))
    print add + "%d = %d" % (cijfer2, cijfer1 + cijfer2)
elif functie == "-":
    minus = "> %d - " % cijfer1
    cijfer2 = int(raw_input(minus))
    print minus + "%d = %d" % (cijfer2, cijfer1 - cijfer2)
elif functie == "*":
    multi = "> %d * " % cijfer1
    cijfer2 = int(raw_input(multi))
    print multi + "%d = %d" % (cijfer2, cijfer1 * cijfer2)
elif functie == "/":
    divide = "> %d / " % cijfer1
    cijfer2 = int(raw_input(divide))
    print divide + "%d = %d" % (cijfer2, cijfer1 / cijfer2)
else:
    print "Invalid option."

