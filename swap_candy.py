from unittest import TestCase
from unittest_data_provider import data_provider

class testCandySwap(TestCase):

    conditions = lambda: (
        ({'list': {'A' : [1,1], 'B' : [2,2]}}, {'result' : [1,2]}),
        ({'list': {'A' : [1,2], 'B' : [2,3]}}, {'result' : [1,2]}),
        ({'list': {'A' : [1,2,5], 'B' : [2,4]}}, {'result' : [5,4]}),
    )
    @data_provider(conditions)
    def test_find_the_way_from_two_destination(self,input,output):

        arrayA = input['list']['A']
        arrayB = input['list']['B']
        result = output['result']
        c = CandySwap()
        self.assertEqual(result, c.findTheCandyForSwapping(arrayA, arrayB))

class CandySwap(object):
    def __init__(self):
        pass

    def findTheCandyForSwapping(self, candyListA, candyListB):
        sumA = 0
        sumB = 0
        for i in candyListA:
            sumA = i + sumA

        dicto = {}
        for i in candyListB:
            sumB = i + sumB
            dicto[i] = 1

        k=0
        for i in candyListA:
            s = sumA - sumB
            y = int(abs((s/2) - i))
            if(y in dicto):
                return [i,y]
            k = k+1
