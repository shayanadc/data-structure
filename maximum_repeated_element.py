from unittest import TestCase
from unittest_data_provider import data_provider

class testLargestSumContiguousSubarray(TestCase):

    conditions = lambda: (
        ({'arr': [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]}, {'result' : 10}),
        ({'arr': [3, 2, 1, 4]}, {'result' : 0}),
        ({'arr': [3, 2, 2,1, 4]}, {'result' : 1}),
    )
    @data_provider(conditions)
    def test_find_the_maximum_distance_two_element(self,input,output):
        array = input['arr']
        result = output['result']
        c = ItemDistance()
        self.assertEqual(result, c.findMaxOfTwoSameItem(array))

class ItemDistance(object):
    def __init__(self):
        pass

    def findMaxOfTwoSameItem(self, arr):
        MAP = {}
        maxDict = 0
        for i in range(len(arr)):
            if arr[i] not in MAP:
                MAP[arr[i]] = i
            else:
                maxDict = max(maxDict, i - MAP[arr[i]])
        return maxDict
