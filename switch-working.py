def main():
	choices = dict(
		one = 'first',
		two = 'second',
		three = 'third'
		)
	v = 'sevne'
	# print(choices[v])
	print(choices.get(v, 'other'))

	a, b = 0, 1

	v = 'This is true' if a < b  else 'this is not ture'
	# if a < b:
	# 	v = 'this is true'
	# else: 
	# 	v = "this is not true"
	print(v)

if __name__ == "__main__": main()