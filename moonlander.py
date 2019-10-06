# Project 2 - Moonlander 
# Author: Ben Clark

# Lunar Lander Simulator

# Units:
# Altitude: m
# Velocity: m/s
# Acceleration: m/s^2
# Fuel: Liters
# Fuel Rate: Liters per second
from landerFuncs import *

showWelcome() # display a welcome message

altitude = getAltitude()
fuel = getFuel()

print("\nLM state at retrorocket cutoff")
elapsedTime = 0
velocity = 0.00
fuel_rate = 0

# show the current state of the moon lander 
displayLMState(elapsedTime, altitude, velocity, fuel, fuel_rate)
print("\n", end='')

fuel_rate = getFuelRate(fuel)

while altitude != 0:

   elapsedTime += 1

   fuel = updateFuel(fuel, fuel_rate)

   acceleration = updateAcceleration(fuel_rate)
   altitude = updateAltitude(altitude, velocity, acceleration)
   velocity = updateVelocity(velocity, acceleration)
   
   if fuel == 0 and altitude != 0:
      # run the following code if the lander runs out of fuel and is at high elevation
      fuel_rate = 0
      string1 = "OUT OF FUEL - Elapsed Time:" + str(elapsedTime).rjust(4) + " "
      string2 = "Altitude:" + format(altitude, ".2f").rjust(8) + " "
      string3 = "Velocity:" + format(velocity, ".2f").rjust(8)
      print(string1 + string2 + string3)
   
   elif altitude != 0:
      # if the lander is at high elevation but has sufficient fuel, 
      # prompt the user to input a new fuel rate
      displayLMState(elapsedTime, altitude, velocity, fuel, fuel_rate)
      print("\n", end='')   
      fuel_rate = getFuelRate(fuel)

# display status at landing
print("\nLM state at landing/impact")
displayLMState(elapsedTime, altitude, velocity, fuel, fuel_rate)
print("\n", end='')
displayLMLandingStatus(velocity)
