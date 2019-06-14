pi = 0;
add = True
n = 1
for i in range(1,500000):
	if i%2==1:
		pi = pi + (4/i)*n
	#	print("Pi: ",pi)
	#	print("4/i: ",4/i*n)
	#	print("i: ",i)
		n = n*-1
print (pi)
