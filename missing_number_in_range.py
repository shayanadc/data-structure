from unittest import TestCase
from unittest_data_provider import data_provider

class testFindMissingNumberInRange(TestCase):

    conditions = lambda: (
        ({'range': [1,3]}, {'result' : 2}),
        ({'range': [1,3,2,5]}, {'result' : 4}),
    )
    @data_provider(conditions)
    def test_find_the_way_from_two_destination(self,input,output):

        ListRange = input['range']
        result = output['result']
        c = MissingNumberInRange()
        self.assertEqual(result, c.findMissingNumberInRange(ListRange))

class MissingNumberInRange(object):
    def __init__(self):
        pass

    def findMissingNumberInRange(self, arr):
        n = len(arr)
        n = n+1
        Sum = n*(n+1)
        Sum = Sum/2
        miss = Sum - sum(arr)
        return miss
