#Implement Queue using Stacks #Leetcode 232
class MyQueue(object):

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def _move_from_in_stack_to_out_stack(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.in_stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if not self.out_stack:
            self._move_from_in_stack_to_out_stack()
        return self.out_stack.pop() if self.out_stack else None
        

    def peek(self):
        """
        :rtype: int
        """
        if not self.out_stack:
            self._move_from_in_stack_to_out_stack()
        return self.out_stack[-1] if self.out_stack else None


    def empty(self):
        """
        :rtype: bool
        """
        if not self.out_stack and not self.in_stack:
            return True
        return False
        
