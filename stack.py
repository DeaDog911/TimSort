from linked_list import LinkedList


class Stack:
    def __init__(self):
        self.lst = LinkedList()

    def push(self, data):
        self.lst.add(data)

    def pop(self):
        return self.lst.remove_last()

    def peek(self):
        return self.lst.get_last()

    def print(self):
        self.lst.print()


if __name__ == "__main__":
    stack = Stack()
    stack.push(5)
    stack.push(9)
    print(stack.peek().data)