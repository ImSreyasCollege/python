class tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def printTree(self, root):
        if(root != None):
            self.printTree(root.left)
            print(root.data, " ")
            self.printTree(root.left)
    def insert(self, root, value):
        if root == None : return tree(value)
        if value < root.data: root.left = self.insert(root.left, value);
        elif value > root.data: root.right = self.insert(root.right, value);
        else : print("Duplicate value");

n = int(input("Enter the no of elements : "))
tree = tree(int(input("Enter the root value : ")))
for i in range(n - 1):
    a = int(input("Enter the element : "))
    tree.insert(tree, a)
print("Data is : ", end="")
tree.printTree(tree)