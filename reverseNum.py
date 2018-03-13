num=int(raw_input(""))
ans=0
while True:
	i=num%10
	ans=ans*10+i
	num=num/10
	if num==0:
		break
print ans
	

