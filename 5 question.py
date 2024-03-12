#Write a program to count the number of a vowel in a string. 
def vowelFunc(str):
	c = 0
	
	s="aeiouAEIOU"
	v = set(s)

	
	for alpha in str:
		
		if alpha in v:
			c = c + 1
	print("Count of Vowels = ", c)


str = input("Enter the string = ")
vowelFunc(str)
