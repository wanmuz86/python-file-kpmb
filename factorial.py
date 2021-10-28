def factorial(n):
	# 1) you have to have a stopper
	if n == 0:
		return 1
	else: 
	# 2) Define a function that will call itself..
		return n * factorial(n-1)

def fib(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fib(n-1)+ fib(n-2)

print(fib(4)) 

