# def main():
# 	fh = open('comment.py')
# 	for line in fh.readlines():
# 		print(line, end=' AMIN ')

# if __name__ == "__main__": main()

# def main():
# 	fh = open('comment.py')
# 	for index, line in enumerate(fh.readline()):
# 		print(index, line, end='')

# if __name__ == "__main__": main()

# def main():
# 	s = "this is a string"
# 	for i, c in enumerate(s):
# 		print(i, c)
# if __name__ == "__main__": main()

def main():
	s = 'this is a string'
	for i, c in enumerate(s):
		if c == "s": print('index {} is an s'.format(i))

if __name__ == "__main__": main()