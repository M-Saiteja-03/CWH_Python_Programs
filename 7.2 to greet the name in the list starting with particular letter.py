'''list=['harini','janaki','satyamurthy','saiteja']
for i in range(len(list)):
    if(list[i][0]=='s'):
        print(f'hello {list[i]}, welcome')
    else:
        continue'''


list=['harini','janaki','satyamurthy','saiteja']
for name in list:
    if name.startswith('s'):
        print('hello '+ name)

        
    
