"""
CP1404/CP5632 Practical
Client code to use the Car class
Note that the import has a folder (module) in it.
"""


from cars import Car


def main():
    limo = Car(100)
    limo.add_fuel(20)
    print("limo fuel =", limo.fuel)
    limo.drive(115)
    print("limo odo =", limo.odometer)
    print(limo)
    bus = Car(180)
    bus.drive(30)
    print("bus fuel =", bus.fuel)
    print("bus odo =", bus.odometer)
    print(bus)

    print("Car {}, {}".format(bus.fuel, bus.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=bus))

main()
