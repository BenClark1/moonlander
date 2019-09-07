# Project 2 - Moonlander

# Author: Ben Clark

def showWelcome():
   welcome_message = """
Welcome aboard the Lunar Module Flight Simulator

   To begin you must specify the LM's initial altitude
   and fuel level.  To simulate the actual LM use
   values of 1300 meters and 500 liters, respectively.

   Good luck and may the force be with you!
"""
   print(welcome_message)
   return
   
def getFuel():
   fuel = input("Enter the initial amount of fuel on board the LM (in liters): ")
   fuel = int(fuel)
   while fuel <= 0:
      print("ERROR: Amount of fuel must be positive, please try again")
      fuel = input("Enter the initial amount of fuel on board the LM (in liters): ")
      fuel = int(fuel)
   return fuel


def getAltitude():
   altitude = float(input("Enter the initial altitude of the LM (in meters): "))
   while altitude < 1 or altitude > 9999:
      print("ERROR: Altitude must be between 1 and 9999, inclusive, please try again")
      altitude = float(input("Enter the initial altitude of the LM (in meters): "))
   return altitude
   
def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):
   print("Elapsed Time:".rjust(13) + (str(elapsedTime) + " s").rjust(7))
   print("Fuel:".rjust(13) + (str(fuelAmount) + " l").rjust(7))
   print("Rate:".rjust(13) + (str(fuelRate) + " l/s").rjust(9))
   print("Altitude:".rjust(13) + (format(altitude, ".2f") + " m").rjust(10))
   print("Velocity:".rjust(13) + (format(velocity, ".2f") + " m/s").rjust(12))
   return

def getFuelRate(currentFuel):
   fuel_rate = input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): ")
   fuel_rate = int(fuel_rate)
   while fuel_rate < 0 or fuel_rate > 9:
      print("ERROR: Fuel rate must be between 0 and 9, inclusive\n")
      fuel_rate = input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): ") 
      fuel_rate = int(fuel_rate)
   return min(fuel_rate, currentFuel)
 
def updateAcceleration(gravity, fuelRate):
   # use 1.62 for gravity when calling this function
   new_acceleration = gravity*((fuelRate/5) - 1)
   return new_acceleration
	
def updateAltitude(altitude, velocity, acceleration):
   # altitude and velocity are current (tp0), acceleration is the new value (tp1)
   new_altitude = float(altitude + velocity + (acceleration/2))
   return max(new_altitude, 0)

def updateVelocity(velocity, acceleration):
   # acceleration is the new value (tp1)
   new_velocity = velocity + acceleration
   return float(new_velocity)

def updateFuel(fuel, fuelRate):
   remaining_fuel = fuel - fuelRate
   return max(0, remaining_fuel)

def displayLMLandingStatus(velocity):
   # print status at landing depending on how fast the lander was moving
   if velocity >= -1 and velocity <= 0:
      print("Status at landing - The eagle has landed!")
   elif velocity > -10 and velocity < -1:
      print("Status at landing - Enjoy your oxygen while it lasts!")
   elif velocity <= -10:
      print("Status at landing - Ouch - that hurt!")
   return
      

