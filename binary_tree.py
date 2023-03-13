class BinaryTree:
    def __init__(self, valor):
        self.key = valor
        self.left_child = None
        self.right_child = None

    def insert_left(self, valor):
        if self.left_child is None:
            self.left_child = BinaryTree(valor)
        else:
            temp = BinaryTree(valor)
            temp.left_child = self.left_child
            self.left_child = temp

    def insert_right(self, valor):
        if self.right_child is None:
            self.right_child = BinaryTree(valor)
        else:
            temp = BinaryTree(valor)
            temp.right_child = self.right_child
            self.right_child = temp

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_root_val(self, valor):
        self.key = valor

    def get_root_val(self):
        return self.key

    def pre_order(self):
        print(self.key)
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()

    def in_order(self):
        if self.left_child:
            self.left_child.in_order()
        print(self.key)
        if self.right_child:
            self.right_child.in_order()

    def pos_order(self):
        if self.left_child:
            self.left_child.pos_order()
        if self.right_child:
            self.right_child.pos_order()
        print(self.key)
