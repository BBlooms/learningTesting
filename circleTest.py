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

class Ellipse:
	' Understands a regular oval shape, traced by a point moving in a plane so that the sum of its distances from two other points (the foci) is constant, or resulting when a cone is cut by an oblique plane that does not intersect the base.'
	def __init__(self, major, minor):
		self.major = major
		self.minor = minor
	def area(self):
		return 3.14*self.major/2*self.minor/2

class Triangle:
	'Understands a plane figure with three straight sides and three angles'
	def __init__(self, side1, side2, side3):
		self.side1 = side1
		self.side2 = side2
		self.side3 = side3
	def perimeter(self):
		return self.side1+self.side2+self.side3

class Line:
	'Understands a straight or curved continuous extent of length without breadth'
	def __init__(self, length):
		self.length = length
	def getLength(self):
		return self.length

class circleTests(unittest.TestCase):
	def testShouldReturnAreaOfCircleWithRadius2(self):
		actual = Circle(2).area()
		expected = 12.56
		self.assertEqual(actual, expected)

	def testShouldReturnCircumferenceOfCircleWithRadius2(self):
		actual = Circle(2).circumference()
		expected = 12.56
		self.assertEqual(actual, expected)

class ellipseTests(unittest.TestCase):
	def testShouldReturnAreaOfEllipseWithMajor7AndMinor5(self):
		actual = Ellipse(7,5).area()
		expected = 27.475
		self.assertEqual(actual, expected)

class triangleTests(unittest.TestCase):
	def testShouldReturnPerimeterOfTriangleWithSidesLength5And6And7(self):
		actual = Triangle(5,6,7).perimeter()
		expected = 18
		self.assertEqual(actual, expected)

class lineTests(unittest.TestCase):
	def testShouldReturnLengthOfLineWithLength8(self):
		actual = Line(8).getLength()
		expected = 8
		self.assertEqual(actual, expected)


def main():
	unittest.main()

if __name__ == "__main__":
	unittest.main()