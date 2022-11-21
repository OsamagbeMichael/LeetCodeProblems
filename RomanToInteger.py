#Roman to  integer 

#Input: A string 
#Output: A set of values that when translated from the string lateral to integer  outputs
#a number 



def romanToInteger(self, s:str)-> str:
	#In roman numerals, there are seven different symbols I,V,X,L,C,D,M
	#We are going to create a dictionary of the values attached to the symbols
	
	RPG{
		"I": 1,
		"V":5,
		"X":10,
		"L":50,
		"C":100,
		"D":500,
		"M":1000
	}




	for i in range(len(s)):
		result = 0

		#we have two conditions: making sure we are in bounds in the string and
		#making sure the roman figure before is greater than the one that comes after it.
		#Int
		if i+1 <len(s) and  RPG[s[i]] > RPG[s[i+1]]:
			result += RPG[s[i]]
		else:
			result -= RPG[s[i]]
	return result  



