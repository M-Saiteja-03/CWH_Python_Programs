mydict={                                           #-->dictionary is a data type which consists of key-value pairs.
    "mycollege":'CBIT',
    "mybranch":"Computer Science and Engineering",
    "myname":'Marepally Saiteja',
    "myroll.no":'167',
    1:3
    }
print(mydict['mycollege'])
print(mydict.keys())
print(mydict.values())
print(mydict.items())
mydict.update({"myphone":"redmi note 8 pro"})
print('\n')
print("the updated dictionary is:",mydict)
print('\n')
print(mydict.get('myname'))
print(mydict['myname'])
print('\n')
print(mydict.get('xyz'))#-->difference between get() and normal extarction is get() does not throw any error and returns none if the key is not available in the dictio
print(mydict['xyz'])    #-->dictionary whereas the normal extraction throws an error


