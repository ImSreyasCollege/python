class A: 
    def __init__(self):
       self.name = "something"
    def display(self):
        print(self.name)

class B(A): 
    def __init__(self, name):
        self.name = name
    def display(self):
        print(self.name)
        super().display()

obj = B("sreyas")
obj.display()