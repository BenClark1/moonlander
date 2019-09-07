import unittest
from landerFuncs import *

class TestCases(unittest.TestCase):
   def test_showWelcome1(self):
      self.assertEqual(showWelcome(), None)

   def test_update_acc1(self):
      self.assertAlmostEqual(updateAcceleration(1.62, 0), -1.62)
   def test_update_acc2(self):
      self.assertAlmostEqual(updateAcceleration(1.62, 20), 4.86)

   def test_updateAlt1(self):
      self.assertEqual(updateAltitude(66666,-22222,-33333), 27777.5) 
   def test_updateAlt2(self):
      self.assertEqual(updateAltitude(1, -10, -10), 0)

   def test_updateVel1(self):
      self.assertAlmostEqual(updateVelocity(11111, 22222.2222), 33333.2222)
   def test_updateVel2(self):
      self.assertEqual(updateVelocity(99999, 0), 99999)

   def test_updateFuel(self):
      self.assertEqual(updateFuel(0, -12.243), -12.243)
   def test_updateFuel(self):
      self.assertEqual(updateFuel(10, 8), 2)
 
      

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

