def main():
	s = 'this is a string'
	# for c in s:
	# 	# if c == "s": continue
	# 	# if c == "s": break
	# 	print(c, end='')

	i = 0
	while(i < len(s)):
		print(s[i], end='')
		i += 1
	else:
		print("else")

if __name__ == "__main__": main()