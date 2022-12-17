#star pattern 1.1
'''for i in range(1,4):
    for j in range(1,i+1):
        print('*',end=' ')
    print('\n')'''
#method 2
'''for i in range(1,4):
    print("*"*i)'''
#star pattern 2
n=int(input("enter no.of lines of stars:"))
for i in range(n):
    print(" "*(n-i-1),end='')
    print("*"*(2*i+1),end='')
    print(' '*(n-i-1))

    
