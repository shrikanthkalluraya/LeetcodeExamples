class RandomizedSet:

    def __init__(self):
        # Stores values:indices
        self.r_map = {}

        # Stores map
        self.r_list = []

    def insert(self, val: int) -> bool:
        if val in self.r_map: return False

        self.r_list.append(val)
        self.r_map[val] = len(self.r_list) - 1

    def remove(self, val: int) -> bool:
        if val not in self.r_map: return False

        # idx = self.r_map[val]
        # self.r_map[self.r_list[-1]] = idx
        # self.r_list[idx] = self.r_list[-1]
        # self.r_map.pop(val)
        # self.r_list.pop()
        del self.r_map[val]
        self.r_list.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.r_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
