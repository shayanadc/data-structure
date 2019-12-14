from unittest import TestCase
from unittest_data_provider import data_provider

class TestBinarySearch(TestCase):

    conditions = lambda: (
        ({'arr': [6,7,8,9], 'n': 9}, {'result' : 2}),
        ({'arr': [1,2,3,4,5,6,7,8,9], 'n': 9}, {'result' : 3}),
        ({'arr': [1,2,3,4,5,6,7,8,9], 'n': 1}, {'result' : 2}),
        ({'arr': [1,2,3,4,5,6,7,8,9,10], 'n': 10}, {'result' : 3}),
    )
    @data_provider(conditions)
    def test_array_with_k_rotation(self,input,output):
        array = input['arr']
        n = input['n']
        result = output['result']
        c = BinarySearch()
        self.assertEqual(result, c.findWithBinarySeach(array,n))

class BinarySearch(object):
    def __init__(self):
        pass

    def findWithBinarySeach(self, array, n):
        first = 0
        last = len(array) - 1
        compare = 0
        while (first <= last and compare <= len(array)/2):
            mid = (first + last) // 2
            if array[mid] == n:
                return compare
            else:
                compare += 1
                if n < array[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
