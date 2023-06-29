"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

from src.stack import *

stack = Stack()
stack.push("data1")


class TestStack(unittest.TestCase):
    def test_changes(self):
        self.assertEqual(stack.pop(), "data1")
        self.assertIsNone(stack.pop())
        self.assertEqual(str(stack),
                         "Класс стека вызовов, который построен на стратегии LIFO (последний вошёл - первым вышел)")
