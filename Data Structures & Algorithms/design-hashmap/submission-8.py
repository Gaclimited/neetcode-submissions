class LL:
    def __init__(self,key,val,next=None):
        self.key=key
        self.val=val
        self.next=next
class MyHashMap:

    def __init__(self):
        self.data=[None]*10

    def put(self, key: int, value: int) -> None:
        index=key%10
        cur=self.data[index]
        while cur:
            if cur.key==key:
                cur.val=value
                return
            cur=cur.next
        new_node=LL(key,value,self.data[index])
        self.data[index]=new_node
        return
        

    def get(self, key: int) -> int:
        index=key%10
        cur=self.data[index]
        while cur:
            if cur.key==key:
                return cur.val
            cur=cur.next
        return -1

    def remove(self, key: int) -> None:
        index=key%10
        cur=self.data[index]
        prev=None
        while cur:
            if cur.key==key:
                if prev==None:
                    self.data[index]=cur.next
                    return
                prev.next=cur.next
                return
            prev=cur
            cur=cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)