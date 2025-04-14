# Min Stack Leet code #155
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
class MinStack(object):

    def __init__(self):
        self.min_stack = []
        self.main_stack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.main_stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            min_top = self.min_stack[-1]
            self.min_stack.append(min(val, min_top))
        

    def pop(self):
        """
        :rtype: None
        """
        if not self.main_stack:
            return None
        self.min_stack.pop()
        return self.main_stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if not self.main_stack:
            return None
        return self.main_stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.min_stack:
            return None
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
