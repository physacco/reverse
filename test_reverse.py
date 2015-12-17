#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import unittest
from random import choice
from string import ascii_letters
from reverse import CHUNK_SIZE, split_size, reverse_file

class TestReverse(unittest.TestCase):
    def setUp(self):
        self.size1 = CHUNK_SIZE // 3
        self.size2 = CHUNK_SIZE * 3
        self.size3 = self.size2 + self.size1

    def test_split_size(self):
        self.assertEqual(split_size(self.size1), [(0, self.size1)])

        self.assertEqual(split_size(self.size2), [(0, CHUNK_SIZE),
            (CHUNK_SIZE, CHUNK_SIZE), (CHUNK_SIZE * 2, CHUNK_SIZE)])

        self.assertEqual(split_size(self.size3), [(0, CHUNK_SIZE),
            (CHUNK_SIZE, CHUNK_SIZE), (CHUNK_SIZE * 2, CHUNK_SIZE),
            (CHUNK_SIZE * 3, self.size1)])

    def test_reverse_file(self):
        self._test_reverse_file_of_size(self.size1)
        self._test_reverse_file_of_size(self.size2)
        self._test_reverse_file_of_size(self.size3)

    def _test_reverse_file_of_size(self, size):
        filename, data = TestReverse.create_file(size)
        rev_filename = filename + '.rev'
        reverse_file(filename, rev_filename)
        with open(rev_filename, 'rb') as f:
            self.assertEqual(f.read(), data[::-1])
        os.unlink(filename)
        os.unlink(rev_filename)

    @staticmethod
    def create_file(size):
        filename = 'test.%d.tmp' % size
        data = ''.join(choice(ascii_letters) for _ in range(size))
        if sys.version_info >= (3, 0, 0):
            data = data.encode() # convert from str to bytes
        with open(filename, 'wb') as f:
            f.write(data)
        return (filename, data)

if __name__ == '__main__':
    unittest.main()
