def one(i):
	lst = [100,200,300,400,20,500,700,00]
	if i != 200:
		raise Exception("Error")
	else:
		print(i+1)
		for i in lst:
			one(i)
one(200)