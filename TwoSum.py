
#Warning not properly indented
#Problem: TwoSum
#Input: A sorted array containing a random input of numbers
#Output: Indices postion of the numbers that add up to the target
#idea
#We can use bruteforce by having two for loops going through the array to get our answer but that is not optimal. So what we are
#going to do is #loop through the array and add each number to a set. Before we add the number to the set, we check for a difference
#between our target number and the value in the array. If that difference is in the set, we have found our digits and all we have to do
#is return the indices of those numbers inthat array
#We are going to use the hashmaps data structure.

def twoSum(self,nums:List[int] , target: int) -> List[int]:
store = {}
#Enumerate() method adds a counter to an iterable and returns it in a form of enumerating
for x,y in enumrate (nums):
	difference = target - y
		if difference in store:
			return [store[difference],x]
		else:
			store[y] = x