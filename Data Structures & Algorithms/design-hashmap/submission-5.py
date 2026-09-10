class MyHashMap:

    def __init__(self):
        self.data=[[] for i in range(10)]

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.data[key%10])):
            if key == self.data[key%10][i][0]:
                self.data[key%10][i][1]=value
                break
        else:
            self.data[key%10].append([key,value])
            

    def get(self, key: int) -> int:
        for i in range(len(self.data[key%10])):
            if key == self.data[key%10][i][0]:
                return self.data[key%10][i][1]
                
        else:
            return -1
                

    def remove(self, key: int) -> None:
        for i in range(len(self.data[key%10])):
            if key == self.data[key%10][i][0]:
                self.data[key%10].pop(i)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)