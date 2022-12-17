def factorial(n):
    if n==1:
        return 1
    fact=n*factorial(n-1)
    return fact

x=int(input("enter the number:"))
fact=factorial(x)
print(f'the factorial of {x} is "{fact}"')

