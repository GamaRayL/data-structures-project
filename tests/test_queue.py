"""Здесь надо написать тесты с использованием unittest для модуля queue."""

import unittest

from src.queue import *

queue = Queue()


class TestQueue(unittest.TestCase):
    def test_changes(self):
        self.assertEqual(str(queue), "")

        queue.enqueue("data1")
        self.assertEqual(queue.head.data, "data1")
        self.assertEqual(str(queue), "data1")

        queue.enqueue('data2')
        self.assertEqual(queue.tail.data, "data2")

        self.assertEqual(queue.dequeue(), None)
