#inpput:  String of letters
#output: Longest palindromic string 

#abba
#bxxxb
def LongestPalindromicSubstring(self, s:str)-> str:

	result = 0 #setting the result variable to store string
	resultLength = ""#length of string

	for i in range(len(s)):
		#checking for even palindromic substring 
		i,i = left, right
		while l>=0 and r<len(s) and s[l] == s[r]:
			if r-l+1 > resultLength:
				res = s[l:r+1]
				resultLength = r-l+1
				l-=1
				r+=1


		#checking for odd palindromic substring 
		i,i = left, right+1
		while l>=0 and r<len(s) and s[l] == s[r]:
			if r-l+1 > resultLength:
				res = s[l:r+1]
				resultLength = r-l+1
				l-=1
				r+=1



	return result







