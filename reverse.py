string=raw_input("")
l=len(string)
print l,string[9]
ans=''
for i in range(l-1,-1,-1):
	print i,string[i]
	ans+=string[i]
print ans