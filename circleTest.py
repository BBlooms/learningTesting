import unittest 
#import circle

class Circle:
	'Understands a round plane figure whose boundary (circumference) consists of points equidistant from a fixed point (the center)'
	def __init__(self, radius):
		self.radius = radius
	def area(self):
		return 3.14*self.radius*self.radius
	def circumference(self):
		return 3.14*self.radius*2

class circleTests(unittest.TestCase):
	def testShouldReturnAreaOfCircleWithRadius2(self):
		actual = Circle(2).area()
		expected = 12.56
		self.assertEqual(actual, expected)

	def testShouldReturnCircumferenceOfCircleWithRadius2(self):
		actual = Circle(2).circumference()
		expected = 12.56
		self.assertEqual(actual, expected)


def main():
	unittest.main()

if __name__ == "__main__":
	unittest.main()