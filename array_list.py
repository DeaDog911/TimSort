class ArrayList:
    def __init__(self, capacity=10):
        self.array = [None]*capacity
        self.size = 0
        self.__capacity = capacity

    def increase_capacity(self):
        self.__capacity = self.__capacity + (self.__capacity >> 1) + 1
        new_array = [None] * self.__capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def add(self, data, index=None):
        if index is not None and (index < 0 or index >= self.size):
            return
        if self.size + 1 > self.__capacity:
            self.increase_capacity()
        if index is None:
            self.array[self.size] = data
            self.size += 1
        else:
            self.size += 1
            for i in range(self.size, index, -1):
                self.array[i] = self.array[i-1]
            self.array[index] = data

    def remove(self, index):
        if index is None or index < 0 or index >= self.size:
            return
        for i in range(index, self.size):
            self.array[i] = self.array[i + 1]
        self.size -= 1

    def get(self, index):
        if index is None or index < 0 or index >= self.size:
            return
        return self.array[index]

    def set(self, index, data):
        if index is None or index < 0 or index >= self.size:
            return
        self.array[index] = data

    def contains(self, data):
        for i in range(self.size):
            if self.array[i] == data:
                return True
        return False

    def print(self):
        for i in range(self.size):
            print(self.array[i], end=' ')
        print()

    # def reverse(self):
    #     new_array = [None]*self.__capacity
    #     i = 0
    #     j = self.size - 1
    #     while i < self.size:
    #         new_array[i] = self.array[j]
    #         i += 1
    #         j -= 1
    #     self.array = new_array

    def reverse(self):
        arr = self.array[:self.size]
        for i in range(self.size):
            self.array[i] = arr[i]

    def sort(self):
        arr = self.array[:self.size]
        arr.sort()
        for i in range(self.size):
            self.array[i] = arr[i]


if __name__ == "__main__":
    lst = ArrayList()
    lst.add(5)
    lst.add(10)
    lst.add(19)
    lst.print()
    lst.reverse()
    lst.print()
