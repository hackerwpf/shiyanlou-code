for i in range(0,100):
	i = i +1
	a = i // 10
	b= i - a*10
	if (a != 7 and b != 7 and i%7 != 0):
		print(i)
	else:
		continue
