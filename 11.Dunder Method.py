class Dunder:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self, n2):
        #return f"{self.num1 + n2.num1}+{self.num2 + n2.num2}i"
        return complex(self.num1 + n2.num1,self.num2 + n2.num2)


n1 = Dunder(2, 4)
n2 = Dunder(4, 8)
print(n1 + n2)