# 散列表查找（哈希表）
class HashTable:
    def __init__(self, size):
        # 使用list保存哈希表元素
        self.elem = [None for i in range(size)]
        self.size = size

    # 散列函数，除留余数法
    def hash(self, key):
        return key % self.size

    # 插入
    def insert_hash(self, key):

        # 散列地址
        address = self.hash(key)
        while self.elem[address]:
            address = (address + 1) % self.size

        # 在指定地址插入key
        self.elem[address] = key

    # 查找
    def search_hash(self, key):

        address = self.hash(key)
        copy = address
        while self.elem[address] != key:
            address = (address + 1) % self.size

            # 地址为空或回到开始的地址
            if not self.elem[address] or address == copy:
                return False

        return True


if __name__ == '__main__':

    alist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    hash_table = HashTable(len(alist))

    for key in alist:
        hash_table.insert_hash(key)

    for key in hash_table.elem:
        print((key, hash_table.elem.index(key)), end='')

    print("\n")
    print(hash_table.search_hash(0))
    print(hash_table.search_hash(9))

