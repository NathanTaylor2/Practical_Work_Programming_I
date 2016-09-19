from prac_8_walkthrough import Car
from prac_8_walkthrough import Taxi
from prac_8_walkthrough import SilverServiceTaxi
from prac_8_walkthrough import UnreliableCar


def main():
    print("Let's Drive!")
    user_input = input("(C)hoose Taxi, (D)rive, (Q)uit").upper()
    if user_input == 'C' or user_input == 'D' or user_input == 'Q':
        if user_input == 'C' or user_input == 'D':
            if user_input == 'C':
                limo = SilverServiceTaxi(Car, 100, 2)
                print("0 - Limo, fuel={}, odo={}, ${}/km, {}km on current fare".format(limo.fuel, limo.odometer,
                                                                                       limo.price_per_km * limo.fanciness,
                                                                                       limo.current_fare_distance))
            else:
                print('Drive')
    else:
        while user_input != 'C' or user_input != 'D' or user_input != 'Q':
            print("Please choose from menu options")
            user_input = input("(C)hoose Taxi, (D)rive, (Q)uit").upper()


main()
