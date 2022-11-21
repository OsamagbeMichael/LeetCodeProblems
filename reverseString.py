#input : string

#Output: string but reverses


#tww pointer method
# have two pointers, one at the end and the the beginning and gradually reduce and increment the pointers 
def reverseString(self,s:List[str]):->None:
	l,r = 0, len(s)-1

	while l<r:
		s[l],s[r]=s[r],s[l]
		l-=1
		r+=1




