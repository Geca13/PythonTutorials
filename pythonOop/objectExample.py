class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 9.99)
print(hamilton.make)
print(hamilton.price)

hamilton.price = 12.79
print(kenwood.price)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)

kenwood.power = 1.5
#print(kenwood.power)
print(Kettle.power_source)
print(hamilton.power_source)
print(kenwood.power_source)

print("switch to atomic")
Kettle.power_source = "atomic"
kenwood.power_source = "gas"
print(kenwood.power_source)
print(hamilton.power_source)