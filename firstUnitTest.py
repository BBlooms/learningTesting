import unittest

def isEven(n):
	return n % 2 == 0

class isEvenTests(unittest.TestCase):

	def testFirstTest(self):
		self.failUnless(isEven(2))

	def testSecondTest(self):
		self.failIf(isEven(1))

def main():
	unittest.main()

if __name__ == '__main__':
	main()