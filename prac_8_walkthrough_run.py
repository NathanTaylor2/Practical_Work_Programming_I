from prac_8_walkthrough import Car
from prac_8_walkthrough import Taxi
from prac_8_walkthrough import UnreliableCar
from prac_8_walkthrough import SilverServiceTaxi

prius_1 = Taxi(Car, 100)
prius_1.drive(40)
print('Trip 1: fuel = {} odo = {} price per km = ${} current fare distance = {} fare cost = ${}'.format(prius_1.fuel,
                                                                                                        prius_1.odometer,
                                                                                                        prius_1.price_per_km,
                                                                                                        prius_1.current_fare_distance,
                                                                                                        prius_1.get_fare()))
prius_1.current_fare_distance = 0
prius_1.drive(100)
print('Trip 2: fuel = {} odo = {} price per km = ${} current fare distance = {} fare cost = ${}'.format(prius_1.fuel,
                                                                                                        prius_1.odometer,
                                                                                                        prius_1.price_per_km,
                                                                                                        prius_1.current_fare_distance,
                                                                                                        prius_1.get_fare()))
bad_car = UnreliableCar(Car, 100, 50)
bad_car.drive(10)
print('Bad Car Trip: fuel = {} odo = {}'.format(bad_car.fuel, bad_car.odometer))

silver_taxi = SilverServiceTaxi(Car, 120, 2)
silver_taxi.drive(10)
print('Silver Taxi Trip : fuel = {} odo = {} price per km = ${} current fare distance = {} fare cost = ${}'.format(
    silver_taxi.fuel, silver_taxi.odometer, silver_taxi.price_per_km, silver_taxi.current_fare_distance,
    silver_taxi.get_fare()))
