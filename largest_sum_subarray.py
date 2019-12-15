from unittest import TestCase
from unittest_data_provider import data_provider

class testLargestSumContiguousSubarray(TestCase):

    conditions = lambda: (
        ({'arr': [-2,-3,4,-1,-2,1,5,-3]}, {'result' : 7}),
    )
    @data_provider(conditions)
    def test_find_largest_sum_contiguous_subarray(self,input,output):
        array = input['arr']
        result = output['result']
        c = LargestSumContiguousSubarray()
        self.assertEqual(result, c.findLargestSumContiguousSubarray(array))

class LargestSumContiguousSubarray(object):
    def __init__(self):
        pass

    def findLargestSumContiguousSubarray(self, array):
        max_so_far = array[0]
        curr_max = array[0]

        for i in range(1, len(array)):
            curr_max = max(array[i], curr_max + array[i])
            max_so_far = max(max_so_far, curr_max)

        return max_so_far
