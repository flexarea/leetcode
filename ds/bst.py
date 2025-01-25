class Tree:
    def __init__(self, val=None):
        self.value = val

        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None

    def isEmpty(self, val):
        return (self.value == None)

    def insertNode(self, val):
        if self.isEmpty(self.value):
            self.value = val
        elif val < self.value:
            self.left.insertNode(val)
        elif val > self.value:
            self.right.insertNode(val)
        else:
            return

    def __str__(self):
        if self.value == None:
            return f"None"
        return f"root={self.value} left={self.left.value} right={self.right.value}"


x = Tree(10)
x.insertNode(4)
print(x)
