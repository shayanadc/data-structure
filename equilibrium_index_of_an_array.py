from unittest import TestCase
from unittest_data_provider import data_provider

class testLargestSumContiguousSubarray(TestCase):

    conditions = lambda: (
        ({'arr': [-7, 1, 5, 2, -4, 3, 0]}, {'result' : 3}),
    )
    @data_provider(conditions)
    def test_find_equilibrium_index_of_an_array(self,input,output):
        array = input['arr']
        result = output['result']
        c = EquilibriumIndexInArray()
        self.assertEqual(result, c.findEquilibriumIndexOfAnArray(array))

class EquilibriumIndexInArray(object):
    def __init__(self):
        pass

    def findEquilibriumIndexOfAnArray(self, arr):
        total_sum = sum(arr)
        leftSum = 0
        for i, num in enumerate(arr):

            total_sum -= num

            if leftSum == total_sum:
                return i
            leftSum += num

        return -1
