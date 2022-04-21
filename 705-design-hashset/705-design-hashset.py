class MyHashSet:

    def __init__(self):
        self.m=set()

    def add(self, key: int) -> None:
        self.m.add(key)
        

    def remove(self, key: int) -> None:
        if key in self.m:
            self.m.remove(key)
        

    def contains(self, key: int) -> bool:
        
        if key in self.m:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)