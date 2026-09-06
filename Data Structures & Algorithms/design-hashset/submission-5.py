class MyHashSet:

    def __init__(self):
        self.data=[[],[],[],[],[],[],[],[],[],[]]

    def add(self, key: int) -> None:
        if key in self.data[key%10]:
            return
        else:
            self.data[key%10].append(key)

    def remove(self, key: int) -> None:
        if key in self.data[key%10]:
            self.data[key%10].remove(key)
        else:
            return

    def contains(self, key: int) -> bool:
        if key in self.data[key%10]:
            return True
        else:
            return False    

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)