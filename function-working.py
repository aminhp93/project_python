# def main():
# 	testfunc(42)

# def testfunc(number, another="fas", onemore=43):
# 	print('This is a test funciton', number, another, onemore)
# 	# pass

# if __name__ == "__main__": main()

def main():
	testfunc(1, 2, 4, 43, 45, 46)

def testfunc(this, that, other, *args):
	print(this, that, other, args)
	for n in args: print(n, end=' ')
	# pass

if __name__ == "__main__": main()