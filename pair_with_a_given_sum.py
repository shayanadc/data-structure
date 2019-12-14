from unittest import TestCase
from unittest_data_provider import data_provider

class TestPairWithGivenSum(TestCase):

    conditions = lambda: (
        ({'arr': [1,2,3,5,7,8,9], 'sum': 10}, {'result' : 3}),
        ({'arr': [1,2,3], 'sum': 4}, {'result' : 1}),
        ({'arr': [1,2,3,4,5], 'sum': 7}, {'result' : 2}),
    )
    @data_provider(conditions)
    def test_find_pair_with_given_Sum(self,input,output):
        array = input['arr']
        sum = input['sum']
        result = output['result']
        c = SearchForGivenSum()
        self.assertEqual(result, c.findPairWithGivenSum(array,sum))

class SearchForGivenSum(object):
    def __init__(self):
        pass
    def findPairWithGivenSum(self, array, sum):
        ys_hmap = {}
        for x in array:
            y = sum - x
            ys_hmap[x] = y
        res = {}
        for x in array:
            if(x in ys_hmap and ys_hmap[x] in ys_hmap):
                if(x == ys_hmap[x]):
                    break
                Min = min(x,ys_hmap[x])
                Max = max(x,ys_hmap[x])
                NStr = str(Min) + str(Max)
                res[NStr] = True

        return len(res)
