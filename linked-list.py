# !/usr/bin/env python
# !-*-coding:utf-8 -*-
# !@Author : fanchg
# !@Time : 2018/7/11

import unittest
from queue import PriorityQueue
import heapq


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def findKthLargest(self, nums, k):
        """
        求数组中第K大的数
        :type nums: List[int]
        :type k: int
        :rtype: int
        """


    def reverseList(self, head):
        """
        :param head:
        :return:
        """
        temp = ListNode(None)
        while head:
            next = head.next
            head.next = temp.next
            temp.next = head
            head = next
        return temp.next

    def detectCycle(self, head):
        """
        :param head: ListNode
        :return: ListNode
        """
        slow = head
        fast = head
        meet = ListNode(None)

        while fast:
            slow = slow.next
            fast = fast.next

            if not fast:
                return None
            fast = fast.next

            if fast == slow:
                meet = fast
                break

        if meet is None:
            return None

        while head and meet:
            if head == meet:
                print(head.val)
                return head
            head = head.next
            meet = meet.next

        return None

    def copyRandomList(self, head):
        """
        Return a deep copy of the linked list
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        ptr = head
        i = 0
        new_map = []
        arr = {}
        while ptr:
            new_map.insert(i, RandomListNode(0))
            arr[ptr] = i
            i += 1
            ptr = ptr.next

        new_map.append(None)
        i = 0
        ptr = head
        while ptr:
            # 连接新链表next指针
            new_map[i].next = new_map[i+1]
            new_map[i].label = ptr.label

            if ptr.random:
                # 根据arr确认原链表random指针的位置
                id = arr[ptr.random]
                new_map[i].random = new_map[id]
            i += 1
            ptr = ptr.next

        print("********** " + str(new_map[0].label))
        return new_map[0]

    def _mergeLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """


class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class MedianFinder:
    """!有问题"""
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = PriorityQueue()
        self.large = PriorityQueue()

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if self.large.empty() or num < self.large.queue[0]:
            self.large._put(num)
        else:
            self.small.put(num)

        if len(self.small.queue) > len(self.large.queue) + 1:
            self.large._put(self.small.queue.pop())
        elif len(self.large.queue) > len(self.small.queue) + 1:
            self.small.put(self.large.queue.pop())

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small.queue) == len(self.large.queue):
            return (self.small.queue[0] + self.large.queue[0])/2
        elif len(self.small.queue) < len(self.large.queue):
            return self.large.queue[0]
        else:
            return self.small.queue[0]


class Testcase(unittest.TestCase):

    def test_queue(self):
        a = MedianFinder()
        a.addNum(-1)
        a.addNum(-2)
        c = a.findMedian()
        print(c)
        a.addNum(-3)
        print(a.findMedian())
        a.addNum(-4)
        print(a.findMedian())
        a.addNum(-5)
        a.addNum(-6)
        print(a.findMedian())

    def test_linked_list(self):
        a = RandomListNode(1)
        b = RandomListNode(3)
        c = RandomListNode(4)
        d = RandomListNode(6)
        e = RandomListNode(7)
        f = RandomListNode(8)

        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f

        a.random = c
        b.random = d
        c.random = c
        d.random = a
        e.random = f
        f.random = e

        solution = Solution().copyRandomList(a)
        # self.assertEqual(solution, a)
        return solution


if __name__ == '__main()__':
    test_su = unittest.TestSuite()
    test_su.addTest(unittest.makeSuite(Testcase))
    unittest.TextTestRunner().run(test_su)
