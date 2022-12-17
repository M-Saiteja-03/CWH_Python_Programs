Letter='''DEAR <|NAME|>,
          CONGRATULATIONS!!YOU ARE HERE BY INFORMED THAT YOU ARE SELECTED IN THE INTERVIEW OF MICROSOFT AND YOU ARE BEING OFFERED WITH THE PACKAGE OF 42.75 LPA!!
          WITH REGARDS,
          BILL GATES
          DATE:<|DATE|>'''
name=input("enter your name:")
date=input("enter the date of selection:")
Letter=Letter.replace("<|NAME|>",name)#-->.replace function returns the replaced/modified string,so it has to be assigned again to the original string and has to be
Letter=Letter.replace("<|DATE|>",date)#-->printed again unlike functions in list
print(Letter)
