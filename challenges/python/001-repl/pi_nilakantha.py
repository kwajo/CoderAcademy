pi = 3
n = 1
for i in range (2,500000,2):
	pi = pi + 4.0/(i*(i+1)*(i+2))*n
	n = n*-1
#	print(pi)
print (pi)
