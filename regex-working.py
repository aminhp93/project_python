# import re

# def main():
# 	fh = open("comment.py")
# 	for line in fh:
# 		match = re.search('(def|a)n', line)
# 		if match:

# 			# print(line, end='')
# 			print(match.group())

# if __name__ == "__main__": main()

import re

def main():
	fh = open("comment.py")
	for line in fh:
		# print(re.sub('(def|a)n','###', line), end='')
		match = re.search('(def|a)n', line)
		if match:
			print(line.replace(match.group(), "amin"), end='')

		
if __name__ == "__main__": main()