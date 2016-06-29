# def main():
# 	try:
# 	fh = open('comsment.py')
# 	except IOError as e:
# 		print('could not open the file', e)
# 	else:
# 		for line in fh: print(line.strip())

# if __name__ == "__main__": main()

def main():
	try: 
		for line in readfile('comment.p1y'): print(line.strip())

	except IOError as e:
		print('cannot read file', e)
	except ValueError as e:
		print('bad filename', e)

def readfile(filename):
	if filename.endswith('py'):
		fh = open(filename)
		return fh.readlines()
	else: raise ValueError('Filename must end with .txt')

if __name__ == "__main__": main()


