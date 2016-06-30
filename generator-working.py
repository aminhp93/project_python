# def main():
# 	print("this is the function/py file")
# 	for i in inclusive_range(5,25,3):
# 		print(i, end=' ')

# def inclusive_range(*args):
# 	numargs = len(args)
# 	if numargs < 1: raise TypeError("requires at least one argument")
# 	elif numargs == 1:
# 		stop = args[0]
# 		start = 0
# 		step = 1 
# 	elif numargs == 2:
# 		(start, stop) = args
# 		step = 1
# 	elif numargs == 3:
# 		(start, stop, step) = args
# 	else: raise TypeError('inclusive_range expected at most 3 argument, got {}'.format(numargs))
# 	i = start
# 	while i <= stop:
# 		yield i
# 		i += step

# if __name__ == "__main__": main()

class inclusive_range:
	def __init__(self, *args):
		numargs = len(args)
		if numargs < 1: raise TypeError("require at least one argument")
		elif numargs == 1:
			self.stop = args[0]
			self.start = 0
			self.step = 1
		elif numargs == 2:
			(self.start, self.stop) = args
			self.step = 1
		elif numargs == 3:
			(self.start, self.stop, self.step) = args
		else: raise TypeError('expected at mmost 3 arguments, got {}'.format(numargs))
		
	def __iter__(self):
		i = self.start
		while i <= self.stop:
			yield i
			i += self.step

def main():
	o = inclusive_range(5, 25, 4)
	# o = range(25)
	for i in o: print(i, end= ' ')

if __name__ == "__main__": main()