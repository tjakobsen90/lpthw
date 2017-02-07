prompt = "> "

print "Welkom bij de rekenmachine."

print "Eerste cijfer:"
cijfer1 = int(raw_input(prompt))

print "Eerste cijfer: %d \nTweede cijfer:" % cijfer1
cijfer2 = int(raw_input(prompt))

print "Eerste cijfer: %d \nTweede cijfer: %d \nFunctie: \n\t1. Aftrekken \n\t2. Optellen \n\t3. Delen \n\t4. Vermedigvuldigen" % (cijfer1, cijfer2)
antwoord = int(raw_input(prompt))

if antwoord == 1:
    aftrekken = cijfer1 - cijfer2
    print "%d - %d = %d" % (cijfer1, cijfer2, aftrekken)
elif antwoord == 2:
    optellen = cijfer1 + cijfer2
    print "%d + %d = %d" % (cijfer1, cijfer2, optellen)
elif antwoord == 3:
    delen = cijfer1 / cijfer2
    print "%d / %d = %d" % (cijfer1, cijfer2, delen)
elif antwoord == 4:
    vermedigvuldigen = cijfer1 * cijfer2
    print "%d * %d = %d" % (cijfer1, cijfer2, vermedigvuldigen)
else:
    print "Dat begreep ik niet."
