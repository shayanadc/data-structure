from unittest import TestCase
from unittest_data_provider import data_provider

class testFindItinerary(TestCase):

    conditions = lambda: (
        ({'map': {'A' : 'B', 'B' : 'C', 'C':'D'}}, {'way' : 'ABCD'}),
        ({'map': {'A' : 'B', 'B' : 'C', 'C':'D', 'D' : 'E'}}, {'way' : 'ABCDE'}),
        ({'map': {'A' : 'B', 'B' : 'C', 'C':'E', 'D' : 'C'}}, {'way' : 'ABCE'}),
    )
    @data_provider(conditions)
    def test_find_the_way_from_two_destination(self,input,output):

        array = input['map']
        result = output['way']
        c = ItemDistance()
        self.assertEqual(result, c.findTheWay(array))

class ItemDistance(object):
    def __init__(self):
        pass

    def findTheWay(self, mp):
        inv_map = {v: k for k, v in mp.items()}
        ik = [*inv_map]
        k = [*mp]
        PossibleStartPoints = (list(set(k) - set(ik)))
        point = PossibleStartPoints[0]
        way = str(point)
        for i in range(len(mp)):
            if(point not in mp):
                break
            else:
                way = way + mp[point]
                point = mp[point]
        return way
