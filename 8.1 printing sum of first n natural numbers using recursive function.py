def sum(n):
    if n==0:
        return 0
    s=n+sum(n-1)
    return s
    

x=int(input("enter the number:"))
s=sum(x)
print(f"the sum of first {x} natural numbers is '{s}'") 
