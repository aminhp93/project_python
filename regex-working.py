import re

def main():
	fh = open("comment.py")
	for line in fh:
		match = re.search('(def|a)n', line)
		if match:

			# print(line, end='')
			print(match.group())

if __name__ == "__main__": main()