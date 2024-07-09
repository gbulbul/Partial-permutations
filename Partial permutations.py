def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1) 
           
def partial_perm(n, k):
	return factorial(n)/factorial(n-k) % 1000000

print(partial_perm(21, 7))