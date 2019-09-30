class BinarySortTreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySortTree:
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def search(self, key):
        bt = self._root
        while bt:
            entry = bt.data
            if key < entry:
                bt = bt.left
            elif key > entry:
                bt = bt.right
            else:
                return entry
        return None

    def insert(self, key):
        bt = self._root
        if not bt:
            self._root = BinarySortTreeNode(key)
            return
        while True:
            entry = bt.data
            if key < entry:
                if bt.left is None:
                    bt.left = BinarySortTreeNode(key)
                    return
                bt = bt.left
            elif key > entry:
                if bt.right is None:
                    bt.right = BinarySortTreeNode(key)
                    return
                bt = bt.right
            else:
                bt.data = key
                return

    def delete(self, key):
        # 维持p为q的父节点
        p, q = None, self._root
        if not q:
            print("空树......")
            return
        while q and q.data != key:
            p = q
            if key < q.data:
                q = q.left
            else:
                q = q.right
            # 当树中没有关键码key时退出
            if not q:
                return
        # 上面已将找到了要删除的节点，用q引用
        # p是q的父节点或者None（q为根节点时）
        if not q.left:
            if p is None:
                self._root = q.right
            elif q is p.left:
                p.left = q.right
            else:
                p.right = q.right
            return

        # 查找节点q的左子树的最右节点，将q的右子树链接为该节点的右子树
        r = q.left
        while r.right:
            r = r.right
        r.right = q.right
        if p is None:
            self._root = q.left
        elif p.left is q:
            p.left = q.left
        else:
            p.right = q.left

    # 二叉树的中序遍历
    def __iter__(self):
        stack = []
        node = self._root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            yield node.data
            node = node.right


if __name__ == '__main__':
    bst = BinarySortTree()
    a = [1, 3, 5, 7, 9, 8, 6, 4, 2]
    for i in range(len(a)):
        bst.insert(a[i])

    # 查找
    asearch = bst.search(7)
    print('\n', asearch)
    for i in bst:
        print(i, end=" ")
    print('\n')

    # 插入、删除
    bst.insert(10)
    bst.delete(1)
    for i in bst:
        print(i, end=" ")

