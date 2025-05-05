def vowel_count(str):
	count = 0
	vowel = set("aeiouAEIOU")
	s=len(str)
	# Write your code here to count the vowels
	for i in range(0,s):
		if str[i] in vowel:
			count+=1
	print(count)
str = input()
vowel_count(str)