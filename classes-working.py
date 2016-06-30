# class Duck:

# 	def __init__(self, value):
# 		print('constructor')
# 		self._v = value

# 	def quack(self):
# 		print("quaack1!!", self._v)

# 	def walk(self):
# 		print("walk like a duck", self._v)

# def main():
# 	donald = Duck(43)
# 	print(donald)
# 	donald.quack()
# 	donald.walk()

# if __name__ == "__main__": main()

# class Duck:

# 	def __init__(self, **kwargs):
# 		self._color = kwargs.get('color', 'white')

# 	def set_color(self,color):
# 		self._color = color

# 	def get_color(self):
# 		return self._color

# def main():
# 	donald = Duck(color = 'blue')
# 	# print(donald._color)
# 	# donald.set_color('blue')
# 	print(donald.get_color())


# if __name__ == "__main__": main()

class Duck:
	def __init__(self, **kwargs):
		self.variables = kwargs

	def set_variables(self, k, v):
		self.variables[k] = v

	def get_variables(self, k):
		return  self.variables.get(k, None)

def main():
	donald = Duck(feet = 2)
	donald.set_variables('color', 'blue')
	print(donald.get_variables('feet'))
	print(donald.get_variables('color'))

if __name__ == "__main__": main()






















