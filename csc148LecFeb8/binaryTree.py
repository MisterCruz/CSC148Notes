class BinaryTree:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        t = BinaryTree(value)
        t.left = self.left
        self.left = t

    def contains(self, value):
        '''(BinaryTree, value) -> bool

        Return True iff value is in self
        '''
        if self.key == value:
            return True
        if self.left != None and self.left.contains(value):
            return True
        if self.right != None and self.right.contains(value):
            return True
        return False
