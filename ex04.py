# cars met een waarde van 100
cars = 100
# ruimte in car met een waarde van 4
space_in_a_car = 4.0
# bestuurders met een waarde van 30
drivers = 30
# passagiers met een waarde van 90
passengers = 90
# niet bereden cars is cars minus bestuurders
cars_not_driven = cars - drivers
# bereden cars is gelijk aan bestuuders
cars_driven = drivers
# mogelijkheid tot carpool capaciteit is bereden cars vermedigvuldigd met de ruimte in de car
carpool_capacity = cars_driven * space_in_a_car
# gemiddelde aantal passagiers in de car is gelijk aan passagiers gedeeld door de bereden cars
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

