from unittest import TestCase
from unittest_data_provider import data_provider

class TestBinarySearch(TestCase):

    conditions = lambda: (
        ({'arr': [2,1,3,5,4], 'n': 5}, {'result' : [3]}),
        ({'arr': [2,1,3,4,6], 'n': 5}, {'result': [4,3]}),
        ({'arr': [1,2,6,4], 'n': 4}, {'result': [2]}),
        ({'arr': [1,2,3,4,5,6,7,8,9], 'n': 9}, {'result': [8,7,6,5,4,3,2]}),
    )
    @data_provider(conditions)
    def test_array_with_k_rotation(self,input,output):
        array = input['arr']
        n = input['n']
        result = output['result']
        c = FindMedianNumbers()
        self.assertEqual(result, c.find(array,n))

class FindMedianNumbers(object):
    def __init__(self):
        pass

    def find(self, array, n):
        result = []
        maxArr = []
        max = array[0]
        for idx, val in enumerate(array):
            if(val> max):
                max = val
                maxArr.insert(idx, 1)
            else:
                maxArr.insert(idx, 0)
        i=n-1
        min = array[i]
        while i>=0:
            if (array[i] < min):
                min = val
                if(maxArr[i] == 1):
                    result.append(array[i])
            i -=1
        return result
