import tree_ex
import bst_printer


class Open_File():
    pass


class Tree(object):
    """Class Tree for binary tree"""

    def __init__(self, val):
        # super(ClassName, self).__init__()
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.__class__.__name__) + ': ' + str(self.__dict__)

    def __repr__(self):
        return str(self.__class__.__name__) + ': ' + str(self.__dict__)


tt = tree_ex.TreeNode(12)
tt.left = tree_ex.TreeNode(5)
tt.left.left = tree_ex.TreeNode(2)
tt.right = tree_ex.TreeNode(4)

bst_printer.bt_print([1, 2, 3, 4, 5])
