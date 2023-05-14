class RandomizedSet:
    # Efficient, but could make it simpler with underlying list instead of dict
    def __init__(self):
        self.numberedDict = {}
        self.choicesDict = {}
        self.size = -1

    def insert(self, val: int) -> bool:
        if val in self.numberedDict:
            return False
        self.size += 1
        self.numberedDict[val] = self.size
        self.choicesDict[self.size] = val
        return True

    def remove(self, val: int) -> bool:
        if val not in self.numberedDict:
            return False
        self.choicesDict[self.numberedDict[val]] = self.choicesDict[self.size]
        self.numberedDict[self.choicesDict[self.size]] = self.numberedDict[val]
        del self.numberedDict[val]
        del self.choicesDict[self.size]
        self.size -= 1
        return True

    def getRandom(self) -> int:
        choice = random.randrange(self.size+1)
        return self.choicesDict[choice]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()