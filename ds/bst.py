class Tree:
    def __init__(self, val=None):
        self.value = val
        if self.value != None:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None

    def isEmpty(self):
        return (self.value == None)

    def insertNode(self, val):
        if self.isEmpty():
            self.value = val
            self.left = Tree()
            self.right = Tree()
        else:
            if val < self.value:
                self.left.insertNode(val)
            elif val > self.value:
                self.right.insertNode(val)
            else:
                return

    def __str__(self):
        if self.isEmpty():
            return "Empty Tree"
        return f"Root={self.value} left={self.left.value} right={self.right.value}"


x = Tree(40)
x.insertNode(10)
x.insertNode(20)
print(x)
