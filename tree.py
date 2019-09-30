class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.root = None  # 父节点


def bulid_tree_line(arr, i):
    if i >= len(arr):
        return None
    node = TreeNode(arr[i])
    node.left = bulid_tree_line(arr, 2*i+1)
    if node.left:
        node.left.root = node
    node.right = bulid_tree_line(arr, 2*i+2)
    if node.right:
        node.right.root = node
    return node


def find_k(node, k):
    if not node:
        return
    print('key', node.val)
    if node.val == k:
        return node
    left = find_k(node.left, k)
    if left.val == k:
        return left
    right = find_k(node.right, k)
    if right.val == k:
        return right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def find(self, value):
        node = self.root
        while node and node.val != value:
            if value == node.val:
                return node
            elif value < node.val:
                node = node.left
            else:
                node = node.right

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
            return
        parent = None
        node = self.root
        while node:
            parent = node
            node = node.left if value < node.val else node.right
        new_node = TreeNode(value)
        if parent.val > value:
            parent.left = new_node
        else:
            parent.right = new_node

    def delete(self, value):
        node = self.root
        parent = None
        while node and node.val != value:
            parent = node
            node = node.left if node.val > value else node.right
        if not node:
            return

        # 要删除的节点有两个子节点
        if node.left and node.right:
            successor = node.right
            successor_parent = node
            while successor.left:
                successor_parent = successor
                successor = successor.left
            node.val = successor.val
            parent, node = successor_parent, successor

        # 删除节点是叶子节点或者仅有一个子节点
        child = node.left if node.left else node.right
        if not parent:
            self.root = child
        elif parent.left == node:
            parent.left = child
        else:
            parent.right = child


# 20190923马蜂窝
# 输入为一个层序遍历的完全二叉树，输出中序遍历下k的下一个值
def build_tree(i, t):
    if i >= len(t):
        return None
    node = TreeNode(t[i])
    node.left = build_tree(2*i+1, t)
    node.right = build_tree(2*i+2, t)
    return node


def get_next(node):
    if not node:
        return -1
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    while node:
        tem = node.next
        if tem.left == node:
            return tem
        node = tem
    return -1


if __name__ == '__main__':
    s = '1,2,3,4,5,6,7,8,9'
    s = list(s.split(','))
    k = '4'
    # s = list(input().split(','))
    # k = input()
    index = s.index(k)
    key = build_tree(index, s)
    print(get_next(key).val)
    root = bulid_tree_line(s, 0)
    node = find_k(root, k)
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        print(node.val)
    else:
        while node.root:
            tem = node.root
            if tem.left == node:
                print(tem.val)
            else:
                node = tem

