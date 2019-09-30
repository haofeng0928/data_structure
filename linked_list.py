class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def append(self, data):
        if isinstance(data, Node):
            pass
        else:
            data = Node(data)
        if not self.head:
            self.head = data
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = data
        self.length += 1

    def delete(self, index):
        if not 0 <= index < self.length:
            print('error: out of index')
            return
        if index == 0:
            self.head = self.head.next
        else:
            p = self.head
            while index-1:
                p = p.next
                index -= 1
            p.next = p.next.next
        self.length -= 1

    def insert(self, index, data):
        if not 0 <= index < self.length:
            print("error: out of index")
            return
        if isinstance(data, Node):
            pass
        else:
            data = Node(data)
        if index == 0:
            data.next = self.head
            self.head = data
        else:
            p = self.head
            while index-1:
                p = p.next
                index -= 1
            data.next = p.next
            p.next = data
        self.length += 1

    def update(self, index, data):
        if not 0 <= index < self.length:
            print('error: out of index')
            return
        if isinstance(data, Node):
            pass
        else:
            data = Node(data)
        if index == 0:
            self.head.data = data
        else:
            p = self.head
            while index:
                p = p.next
                index -= 1
            p.data = data

    def get_data(self, index):
        if not 0 <= index < self.length:
            print("error: out of index")
            return
        if index == 0:
            return self.head.data
        else:
            p = self.head
            while index:
                p = p.next
                index -= 1
            return p.data

    def get_length(self):
        return self.length

    def clear(self):
        self.head = None
        self.length = 0

    def print_list(self):
        if self.length == 0:
            return None
        else:
            p = self.head
            while p.next:
                print(p.data, '->', end=' ')
                p = p.next
            print(p.data)


if __name__ == '__main__':
    a, b, c, d, e = Node(1), Node(2), Node(3), Node(4), Node(5)
    s = LinkedList()

    s.append(a)
    s.append(b)
    s.append(c)
    print(s.head.data, s.head.next.data, s.head.next.next.data)
    s.print_list()

    s.insert(2, e)
    s.print_list()

    s.delete(0)
    s.print_list()

    s.update(0, 1)
    s.print_list()

    print(s.get_data(0))
    print(s.get_length())

