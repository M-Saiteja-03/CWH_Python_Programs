sub1=int(input("enter 1st subject marks:"))
sub2=int(input("enter 2nd subject marks:"))
sub3=int(input("enter 3rd subject marks:"))
if((sub1+sub2+sub3)/3>=40):
    if(sub1>33 and sub2>33 and sub3>33):
        print("pass")
    else:
        print("fail")
        
else:
    print("fail")


    
    
