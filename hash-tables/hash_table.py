

class hash_table:
    def __init__(self):
        self.length = 3
        self.table = [None] * self.length

    def get_hash_index(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.length

    def add(self, key, value):
        index = self.get_hash_index(key)
        key_value = [key, value]
        if self.table[index] is None:
            self.table[index] = [key_value]
        else:
            for elements in self.table[index]:
                if elements[0] == key_value[0]:
                    elements[1] = key_value[1]
                    return
            self.table[index].append(key_value)
        return

    def lookup(self, key):
        index = self.get_hash_index(key)
        if self.table[index] is None:
            return None
        else:
            for elements in self.table[index]:
                if elements[0] == key:
                    return elements[1]

    def remove(self, key):
        index = self.get_hash_index(key)
        if self.table[index] is None:
            return None
        else:
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:
                    self.table[index].pop(i)
                    return


if __name__ == "__main__":
    table = hash_table()
    table.add("Sam", 21)
    table.add("John", 18)
    table.add("Luke", 15)
    table.add("Kevin", 12)
    table.add("Hannah", 21)


    print("Table:\n", table.table)
    print("Sam's Age:", table.lookup("Sam"))
    print("Hannah's Age:", table.lookup("Hannah"))
    print("John's Age:", table.lookup("John"))

    table.remove("Luke")
    print("Updated Table:\n", table.table)

    table.remove("Sam")
    print("Updated Table:\n", table.table)

    table.add("Sam", 21)
    print("Updated Table:\n", table.table)

