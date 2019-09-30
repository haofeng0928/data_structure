class Node(object):

    def __init__(self, data, pnext=None):
        self.data = data
        self.next = pnext

    def __repr__(self):
        return str(self.data)


class ChainTable(object):

    def __init__(self):
        self.head = None
        self.length = 0

    # 判断链表是否为空
    def isEmpty(self):
        return (self.length == 0)

    # 添加链表元素
    def append(self, dataOrNode):
        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if not self.head:
            self.head = item
            self.length += 1
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = item
            self.length += 1

    # 删除链表元素
    def delete(self, index):
        if self.isEmpty():
            print("this chain table is empty.")
            return

        if index < 0 or index >= self.length:
            print('error: out of index')
            return

        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        j = 0
        node = self.head
        prev = self.head
        while node.next and j < index:
            prev = node
            node = node.next
            j += 1

        if j == index:
            prev.next = node.next
            self.length -= 1

    # 插入链表元素
    def insert(self, index, dataOrNode):
        if self.isEmpty():
            print("this chain tabale is empty")
            return

        if index < 0 or index >= self.length:
            print("error: out of index")
            return

        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if index == 0:
            item.next = self.head
            self.head = item
            self.length += 1
            return

        j = 0
        node = self.head
        prev = self.head
        while node.next and j < index:
            prev = node
            node = node.next
            j += 1

        if j == index:
            item.next = node
            prev.next = item
            self.length += 1

    # 更新某元素
    def update(self, index, data):
        if self.isEmpty() or index < 0 or index >= self.length:
            print('error: out of index')
            return
        j = 0
        node = self.head
        while node.next and j < index:
            node = node.next
            j += 1

        if j == index:
            node.data = data

    # 获取链表内容
    def getItem(self, index):
        if self.isEmpty() or index < 0 or index >= self.length:
            print("error: out of index")
            return
        j = 0
        node = self.head
        while node.next and j < index:
            node = node.next
            j += 1

        return node.data

    # 查找某元素位置
    def getIndex(self, data):
        j = 0
        if self.isEmpty():
            print("this chain table is empty")
            return
        node = self.head
        while node:
            if node.data == data:
                return j
            node = node.next
            j += 1

        if j == self.length:
            print("%s not found" % str(data))
            return

    # 清空链表
    def clear(self):
        self.head = None
        self.length = 0

    def __repr__(self):
        if self.isEmpty():
            print("empty chain table")
        node = self.head
        nlist = ''
        while node:
            nlist += str(node.data) + ' '
            node = node.next
        return nlist

    def __getitem__(self, ind):
        if self.isEmpty() or ind < 0 or ind >= self.length:
            print("error: out of index")
            return
        return self.getItem(ind)

    def __setitem__(self, ind, val):
        if self.isEmpty() or ind < 0 or ind >= self.length:
            print("error: out of index")
            return
        self.update(ind, val)

    def __len__(self):
        return self.length


class Solution:
    def printListFromTailToHead(self, Node):
        out = []
        if Node is None:
            return out
        while Node.next is not None:
            out.append(Node.data)
            Node = Node.next
        out.append(Node.data)
        out.reverse()
        return out


lianbiao = ChainTable()

# 创建链表

for i in range(9):
    lianbiao.append(i)
print(lianbiao)

# 从头到尾打印链表

s = Solution()
l = s.printListFromTailToHead(lianbiao.head)
for i in l:
    print(i)
