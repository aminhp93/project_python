class Duck:
	def quack(self):
		print("quaack1!!")

	def walk(self):
		print("walk like a duck")

def main():
	donald = Duck()
	print(donald)
	donald.quack()
	donald.walk()

if __name__ == "__main__": main()