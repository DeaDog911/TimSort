class Node:
    def __init__(self, nxt, data):
        self.nxt = nxt
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data, index=None):
        if index is not None and index < 0:
            return
        new_node = Node(None, data)
        if self.head is None:
            self.head = new_node
        else:
            if index is not None and index == 0:
                new_node.nxt = self.head
                self.head = new_node
            else:
                last_node = self.head
                while last_node.nxt:
                    if index is not None:
                        index -= 1
                        if index == 0:
                            break
                    last_node = last_node.nxt
                if index is not None and index == 0:
                    new_node.nxt = last_node.nxt
                last_node.nxt = new_node

    def print(self):
        last_node = self.head
        while last_node:
            print(last_node.data, end=' ')
            last_node = last_node.nxt
        print()

    def get(self, index):
        last_node = self.head
        if index == 0:
            return self.head
        while last_node.nxt:
            index -= 1
            if index == 0:
                break
            last_node = last_node.nxt
        if index == 0:
            return last_node.nxt
        return None

    def remove(self, index):
        if index == 0:
            self.head = self.head.nxt
        if index > 0:
            prev = self.get(index-1)
            if prev is not None:
                prev.nxt = prev.nxt.nxt

    def get_last(self):
        if self.head is None:
            return None
        last_node = self.head
        while last_node.nxt:
            last_node = last_node.nxt
        return last_node

    def remove_last(self):
        if not self.head:
            return None
        if not self.head.nxt:
            el = self.head
            self.head = None
            return el
        last_node = self.head
        prev = None
        while last_node.nxt:
            prev = last_node
            last_node = last_node.nxt
        el = last_node
        prev.nxt = None
        return el

    def contains(self, data):
        last_node = self.head
        while last_node:
            if last_node.data == data:
                return True
            last_node = last_node.nxt
        return False

    def set(self, index, data):
        last_node = self.head
        if index == 0:
            self.head.data = data
        while last_node.nxt:
            index -= 1
            if index == 0:
                break
            last_node = last_node.nxt
        if index == 0:
            last_node.nxt.data = data

from array_list import ArrayList
if __name__ == '__main__':
    lst = LinkedList()
    lst2 = ArrayList()
    lst2.add(1)
    lst2.add(2)
    lst.add(lst2)
    lst.get(0).data.print()
