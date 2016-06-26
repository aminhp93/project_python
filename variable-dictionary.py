def main():
	# d = {"one": 1, "two": 2, "three": 3}

	d = dict(
		one = 1, two = 2, three = 3, five = 'five'
		)

	d['seven'] = 7
	for k in sorted(d.keys()):
		print(k, d[k])

if __name__ == "__main__": main()