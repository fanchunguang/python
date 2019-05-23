# !/usr/bin/env python
# !-*-coding:utf-8 -*-
# !@Author : fanchg
# !@Time : 2018/7/26
"""

"""
import unittest


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data_queue = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.data_queue.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        m = self.data_queue.pop()
        return m

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if len(self.data_queue) == 0:
            return False
        else:
            return self.data_queue[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.data_queue) == 0


class MyQueue(object):  #
    def __init__(self):
        """
        Initialize your data structure here.
        """
        #self.stack = MyStack()
        self._input = MyStack()
        self._output = MyStack()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self._input.push(x)
        # temp = MyStack()
        # while not self.stack.empty():
        #     temp.push(self.stack.pop())
        # temp.push(x)
        # while not temp.empty():
        #     self.stack.push(temp.pop())
        # return self.stack

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        MyQueue.adjust(self)
        if not self._output.empty():
            x = self._output.top()
            self._output.pop()
            return x
        # if not self.stack.empty():
        #     m = self.stack.pop()
        #     return m

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        # return self.stack.top()
        MyQueue.adjust(self)
        return self._output.top()

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self._input.empty() and self._output.empty()

    def adjust(self):
        """
        adjust the queue
        :return:
        """
        if not self._output.empty():
            return
        while not self._input.empty():
            self._output.push(self._input.top())
            self._input.pop()


class testCase(unittest.TestCase):

    def test_stack(self):
        s = MyQueue()
        s.push(1)
        s.push(2)
        s.push(3)
        s.pop()
        s.push(4)
        s.push(5)
        print(s)
        param_1 = s.pop()
        print("*********param_1 :" + str(param_1))
        param_2 = s.top()
        print("*********param_2 :" + str(param_2))
        param_3 = s.empty()
        print("*********param_3 :" + str(param_3))


if __name__ == '__main__':
    unittest.main()