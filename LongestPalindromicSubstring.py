#inpput:  String of letters
#output: Longest palindromic string 



#caveat of this problem is that string could be even length or odd length and well need to make sure we take care of that caveat
#abba
#bxxxb
def LongestPalindromicSubstring(self, s:str)-> str:

	result = 0 #setting the result variable to store string
	resultLength = ""#length of string


	#looping through the string 
	for i in range(len(s)):
		#checking for even palindromic substring 
		left,right = i, i #setting the left and right indices 

		while l>=0 and r<len(s) and s[l] == s[r]:#loop condition 
			if r-l+1 > resultLength:#if the string is greater than the one we already have
				res = s[l:r+1]#set new string 
				resultLength = r-l+1 #set new string length 
				l-=1
				r+=1


		#checking for odd palindromic substring 
		left,right = i ,i+1
		while l>=0 and r<len(s) and s[l] == s[r]:
			if r-l+1 > resultLength:
				res = s[l:r+1]
				resultLength = r-l+1
				l-=1
				r+=1



	return result#return result







