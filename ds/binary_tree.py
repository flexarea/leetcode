class Tree:
    def __init__(self, val=None):
        self.value = val

        if self.value is not None:
            self.left = Tree()
            self.right = Tree()
        else:
            self.right = None
            self.left = None

    def isEmpty(self):
        return self.value is None

    def insertNode(self, val):
        if self.isEmpty():
            self.value = val
        elif val < self.value:
            if self.left.value is None:
                self.left = Tree(val)
            else:
                self.left.insertNode(val)
        elif val > self.value:
            if self.right.value is None:
                self.right = Tree(val)
            else:
                self.right.insertNode(val)
        else:
            return

    def traversal(self):
        if self.isEmpty():
            return
        self.left.traversal()
        print(self.value)
        self.right.traversal()

    def __str__(self):
        if self.value is None:
            return f"None"
        return f"root={self.value} left={self.left.value} right={self.right.value}"


x = Tree(10)
x.insertNode(12)
x.insertNode(4)
x.traversal()
