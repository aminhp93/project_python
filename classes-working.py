class Duck:

	def __init__(self, value):
		print('constructor')
		self._v = value

	def quack(self):
		print("quaack1!!", self._v)

	def walk(self):
		print("walk like a duck", self._v)

def main():
	donald = Duck(43)
	print(donald)
	donald.quack()
	donald.walk()

if __name__ == "__main__": main()