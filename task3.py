n = int(input("Enter the number of terms: "))
n1 = 0
n2 = 1
c = 0
if n <= 0:
	print("Enter a positive number: ")
elif n == 1:
	print(" Fibonacci series upto" ,n, ":")
	print(n1)
else:
	print("Fibonacci series :")
	while c < n:
		print(n1)
		nth = n1 + n2
		n1 = n2
		n2 = nth
		c = c + 1


