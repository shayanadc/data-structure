from unittest import TestCase
from unittest_data_provider import data_provider

class TestArray(TestCase):

    conditions = lambda: (
        ({'arr': [1,2,3,4,5,6,7,8,9], 'k': 2}, {'result' : [3,4,5,6,7,8,9,1,2]}),
        ({'arr': [1,2,3,4,5,6,7,8,9], 'k': 3}, {'result' : [4,5,6,7,8,9,1,2,3]}),
        ({'arr': [1,2,3,4,5,6,7,8,9], 'k': 1}, {'result' : [2,3,4,5,6,7,8,9,1]}),
        ({'arr': [1,2,3,4,5,6,7,8,9], 'k': 4}, {'result' : [5,6,7,8,9,1,2,3,4]}),
    )
    @data_provider(conditions)
    def test_array_with_k_rotation(self,input,output):
        array = input['arr']
        n = input['k']
        result = output['result']
        c = ArrayDS()
        self.assertEqual(result, c.rotation(array,n))

class ArrayDS(object):
    def __init__(self):
        pass

    def rotation(self, array, n):
        result = array[n:]
        return result + array[0:n]
