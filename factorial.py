val=int(raw_input(""))
def fact(num):
	if num in [0,1]:
		return 1
	return num*fact(num-1)
print fact(val)
