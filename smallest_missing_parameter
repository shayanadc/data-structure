from unittest import TestCase
from unittest_data_provider import data_provider

class TestSmallestMissing(TestCase):

    conditions = lambda: (
        ({'arr': [0, 1, 2, 6, 9], 'n': 5, 'm': 10}, {'result' : 3}),
        ({'arr': [0, 1, 2, 3], 'n': 4, 'm': 5}, {'result' : 4}),
        ({'arr': [0, 1, 2, 3, 4, 5, 6, 7, 10], 'n': 9, 'm': 11}, {'result' : 8}),
    )
    @data_provider(conditions)
    def test_find_smallest_in_array(self,input,output):
        array = input['arr']
        n = input['n']
        m = input['m']
        result = output['result']
        c = SmallestMissingParam()
        self.assertEqual(result, c.findSmallestMissingAmongArray(array,n,m))

class SmallestMissingParam(object):
    def __init__(self):
        pass

    def findSmallestMissingAmongArray(self, array, n, m):

        return self.findFirstMissing(array, array[0], array[n-1])

    def findFirstMissing(self, array, start, end):

        if (start > end):
            return end + 1

        if (start != array[start]):
            return start
        mid = int((start + end) / 2)
        if (array[mid] == mid):
            return self.findFirstMissing(array, mid+1, end)

        return self.findFirstMissing(array,start, mid)
