def stripping(string,word):
    newstr=string.replace(word,' ')
    print(newstr)
    return newstr.strip()
text='hello world'
x='world'
n=stripping(text,x)
print(n)



