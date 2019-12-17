from unittest import TestCase
from unittest_data_provider import data_provider

class testBalancedBrackets(TestCase):


    conditions = lambda: (
        ({'brackets': '{}'}, {'result' : 'Balanced'}),
        ({'brackets': '{}()'}, {'result' : 'Balanced'}),
        ({'brackets': '{}(}'}, {'result' : 'UnBalanced'}),
        ({'brackets': '{[()]}'}, {'result' : 'Balanced'}),
        ({'brackets': '{[(])}'}, {'result' : 'UnBalanced'}),
        ({'brackets': '{{[[(())]]}}'}, {'result' : 'Balanced'}),
    )
    @data_provider(conditions)
    def test_balanced_brackets_with_stack(self, input, output):
        c = BalancedBracket()
        self.assertEqual(output['result'], c.isBalanced(input['brackets']))


class BalancedBracket(object):

    def __init__(self):
        pass

    def isValidPair(self,left, right):
        if left == '(' and right == ')':
            return True
        if left == '[' and right == ']':
            return True
        if left == '{' and right == '}':
            return True
        return False

    def isBalanced(self,bracket):
        stack = []

        open_tup = tuple('({[')
        close_tup = tuple(')}]')
        map = dict(zip(open_tup, close_tup))

        for symbol in bracket:
            if symbol in open_tup:
                stack.append(symbol)
            else:
                if len(stack) == 0 or (map[stack.pop()] != symbol):
                    return 'UnBalanced'

        return 'Balanced'





