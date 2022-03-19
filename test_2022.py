import unittest

import networkx as nx

import work2022


class TestFinal2022(unittest.TestCase):
    # # 1111111111111111 doesn't work
    # print(print_SCCs({1: 'a',
    #                   2: 'b',
    #                   3: 'c',
    #                   4: 'd',
    #                   5: 'e'}, {1: [{'c', 'e'}],
    #                             2: ['a', 'd'],
    #                             3: ['a'],
    #                             4: [{'b', 'c'}],
    #                             5: ['d']}))
    def test_two(self):
        PreferenceListsValues = {1: {'a': 3, 'b': 3}, 2: {'a': 5, 'b': 1}}
        PreferenceLists = {1: [{'a', 'b'}],
                   2: ['a', 'b']}
        house = {1: 'a',
         2: 'b'}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'b', 2: 'a'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'b', 2: 'a'})

        PreferenceListsValues = {1: {'b': 3, 'a': 2}, 2: {'c': 5, 'b': 1}, 3:{'d':9, 'c':8},4:{'d':3}}
        PreferenceLists = {1: ['b', 'a'],
                          2: ['c', 'b'],
                          3: ['d', 'c'],
                          4: ['d']}
        house = {1: 'a',
                         2: 'b',
                         3: 'c',
                         4: 'd'
                 }
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'a', 2: 'b', 3: 'c', 4: 'd'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'a', 2: 'b', 3: 'c', 4: 'd'})

        PreferenceListsValues = {1: {'b': 3, 'a': 2}, 2: {'c': 5, 'b': 1}, 3:{'d':9, 'c':8},4:{'a':3}}
        PreferenceLists = {1: ['b', 'a'],
                           2: ['c', 'b'],
                           3: ['d', 'c'],
                           4: ['a']}
        house = {1: 'a',
                 2: 'b',
                 3: 'c',
                 4: 'd'
                 }
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'b', 2: 'c', 3: 'd', 4: 'a'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'b', 2: 'c', 3: 'd', 4: 'a'})

        PreferenceListsValues = {1: {'b': 3}, 2: {'a': 5}, 3:{'c':9}}
        PreferenceLists = {1: ['b'],
                           2: ['a'],
                           3: ['c']}
        house = {1: 'a',
         2: 'b',
         3: 'c'}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'b', 2: 'a', 3: 'c'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'b', 2: 'a', 3: 'c'})

        PreferenceListsValues = {1: {'a': 2}, 2: {'b': 1}, 3:{'c':8}}
        PreferenceLists = {1: ['a', 'b'],
                  2: ['b', 'a'],
                  3: ['c']}
        house = {1: 'a',
                 2: 'b',
                 3: 'c'}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'a', 2: 'b', 3: 'c'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'a', 2: 'b', 3: 'c'})

        PreferenceListsValues = {1: {'c': 3, 'e': 3}, 2: {'a': 5}, 3: {'a': 2, 'd': 2}, 4: {'b': 3, 'c': 3}, 5: {'d': 5, 'b': 1}}
        house = {1: 'a',
                 2: 'b',
                 3: 'c',
                 4: 'd',
                 5: 'e'}
        PreferenceLists = {1: [{'c', 'e'}],
                           2: ['a'],
                           3: [{'a', 'd'}],
                           4: [{'b', 'c'}],
                           5: ['d', 'b']}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'e', 2: 'a', 3: 'd', 4: 'c', 5: 'b'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'e', 2: 'a', 3: 'd', 4: 'c', 5: 'b'})


        PreferenceListsValues = {1: {'b': 3, 'a': 1}, 2: {'a': 5, 'b':2}}
        house = {1: 'a',
                 2: 'b'}
        PreferenceLists = {1: ['b', 'a'],
                           2: ['a', 'b']}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'b', 2: 'a'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'b', 2: 'a'})

        PreferenceListsValues = {1: {'b': 3, 'a': 3}, 2: {'a': 5, 'b':2}}
        PreferenceLists = {1: [{'a', 'b'}],
                           2: ['a', 'b']}
        house = {1: 'a',
                 2: 'b'}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'b', 2: 'a'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'b', 2: 'a'})

        PreferenceListsValues = {1: {'a': 1}, 2: {'c': 5}, 3: {'b': 5}}
        PreferenceLists = {1: ['a'],
                           2: ['c'],
                           3: ['b']}
        house = {1: 'a',
                 2: 'b',
                 3: 'c'}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'a', 2: 'c', 3: 'b'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'a', 2: 'c', 3: 'b'})

        PreferenceListsValues = {1: {'a': 1, 'b':1}, 2: {'a': 1, 'b':1}}
        PreferenceLists = {1: [{'a', 'b'}],
                           2: [{'a', 'b'}]}
        house = {1: 'a',
                 2: 'b'}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'a', 2: 'b'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'a', 2: 'b'})

        PreferenceListsValues = {1: {'a': 1, 'b':3}, 2: {'a': 4, 'b':1}}
        PreferenceLists = {1: ['b', 'a'],
                           2: ['a', 'b']}
        house = {1: 'a',
                 2: 'b'}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'b', 2: 'a'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'b', 2: 'a'})

        PreferenceListsValues = {1: {'a': 3, 'b': 3}, 2: {'a': 5, 'd': 2}, 3: {'a': 9, 'e':3}, 4: {'b': 3, 'c': 1}, 5: {'d': 5}}
        PreferenceLists = {1: [{'a', 'b'}],
                      2: ['a', 'd'],
                      3: ['a', 'e'],
                      4: ['b', 'c'],
                      5: ['d']}
        house = {1: 'a',
                     2: 'b',
                     3: 'c',
                     4: 'd',
                     5: 'e'}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'b', 2: 'a', 3: 'e', 4: 'c', 5: 'd'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'b', 2: 'a', 3: 'e', 4: 'c', 5: 'd'})

        PreferenceListsValues = {1: {'a': 1, 'b': 1, 'c': 1}, 2: {'a': 8, 'b': 5, 'c': 6}, 3: {'a': 4, 'b': 1, 'c': 7}}
        PreferenceLists = {1: [{'a', 'b', 'c'}],
                  2: ['a', 'c', 'b'],
                  3: ['c', 'a', 'b']}
        house = {1: 'a',
                 2: 'b',
                 3: 'c'}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'b', 2: 'a', 3: 'c'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'b', 2: 'a', 3: 'c'})

        PreferenceListsValues = {1: {'b': 9, 'a': 8, 'c': 7, 'd': 6}, 2: {'a': 5, 'd': 4, 'c': 3, 'b': 2}, 3: {'a': 6, 'd': 5, 'c': 4, 'b': 3}, 4: {'a': 9, 'c': 5, 'd': 4, 'b' :3}}
        PreferenceLists = {1: ['b', 'a', 'c', 'd'],
                  2: ['a', 'd', 'c', 'b'],
                  3: ['a', 'd', 'c', 'b'],
                  4: ['a', 'c', 'd', 'b']}
        house = {1: 'a',
                 2: 'b',
                 3: 'c',
                 4: 'd'}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'b', 2: 'a', 3: 'd', 4: 'c'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'b', 2: 'a', 3: 'd', 4: 'c'})

        PreferenceListsValues = {1: {'a': 3, 'b':3}, 2: {'a': 4, 'b':1}}
        PreferenceLists = {1: [{'a', 'b'}],
                  2: ['a', 'b']}
        house = {1: 'a',
                 2: 'b'}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'b', 2: 'a'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'b', 2: 'a'})

        PreferenceListsValues = {1: {'a': 1}, 2: {'c': 6}, 3: {'b': 1}}
        PreferenceLists = {1: ['a'],
                  2: ['c'],
                  3: ['b']}
        house = {1: 'a',
                 2: 'b',
                 3: 'c'}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'a', 2: 'c', 3: 'b'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'a', 2: 'c', 3: 'b'})

        PreferenceListsValues = {1: {'a': 3, 'b':3}, 2: {'a': 4, 'b':4}}
        PreferenceLists = {1: [{'a', 'b'}],
                  2: [{'a', 'b'}]}
        house = {1: 'a',
                 2: 'b'}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'a', 2: 'b'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'a', 2: 'b'})

        PreferenceListsValues = {1: {'a': 3, 'b':5}, 2: {'a': 4, 'b':1}}
        PreferenceLists = {1: ['b', 'a'],
                  2: ['a', 'b']}
        house = {1: 'a',
                 2: 'b'}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'b', 2: 'a'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'b', 2: 'a'})

        PreferenceListsValues = {1: {'a': 3, 'b':2}, 2: {'a': 4, 'b':1}}
        PreferenceLists = {1: ['a', 'b'],
                  2: ['a', 'b']}
        house = {1: 'a',
                 2: 'b'}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'a', 2: 'b'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'a', 2: 'b'})

        PreferenceListsValues = {1: {'a': 3, 'b':2}, 2: {'a': 4, 'b':1}}
        PreferenceLists = {1: ['a', 'b'],
                  2: ['a', 'b']}
        house = {1: 'a',
                 2: 'b'}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'a', 2: 'b'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'a', 2: 'b'})

        PreferenceListsValues = {1: {'a': 3, 'b': 2}, 2: {'b': 6, 'a': 3}, 3: {'c': 1}}
        PreferenceLists = {1: ['a', 'b'],
                  2: ['b', 'a'],
                  3: ['c']}
        house = {1: 'a',
                 2: 'b',
                 3: 'c'}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'a', 2: 'b', 3: 'c'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'a', 2: 'b', 3: 'c'})

        PreferenceListsValues = {1: {'a': 3, 'b': 3, 'c': 3}, 2: {'a': 3, 'b': 3, 'c': 3}, 3: {'a': 3, 'b': 3, 'c': 3}}
        PreferenceLists = {1: [{'a', 'b', 'c'}],
                  2: [{'a', 'b', 'c'}],
                  3: [{'a', 'b', 'c'}]}
        house = {1: 'a',
                 2: 'b',
                 3: 'c'}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'a', 2: 'b', 3: 'c'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'a', 2: 'b', 3: 'c'})

        PreferenceListsValues = {1: {'b': 2}, 2: {'c': 6}, 3: {'a': 1}}
        PreferenceLists = {1: ['b'],
                  2: ['c'],
                  3: ['a']}
        house = {1: 'a',
                 2: 'b',
                 3: 'c'}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'b', 2: 'c', 3: 'a'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'b', 2: 'c', 3: 'a'})

        PreferenceListsValues = {1: {'b': 2}, 2: {'a': 6}, 3: {'c': 1}}
        PreferenceLists = {1: ['b'],
                  2: ['a'],
                  3: ['c']}
        house = {1: 'a',
                 2: 'b',
                 3: 'c'}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'b', 2: 'a', 3: 'c'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'b', 2: 'a', 3: 'c'})

        PreferenceListsValues = {1: {'a': 2}, 2: {'c': 6}, 3: {'b': 1}}
        PreferenceLists = {1: ['a'],
                  2: ['c'],
                  3: ['b']}
        house = {1: 'a',
                 2: 'b',
                 3: 'c'}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'a', 2: 'c', 3: 'b'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'a', 2: 'c', 3: 'b'})

        PreferenceListsValues = {1: {'a': 5, 'b': 4, 'c': 3, 'd': 2}, 2: {'a': 5, 'b': 4, 'c': 3, 'd': 2}, 3: {'a': 5, 'b': 4, 'c': 3, 'd': 2}
                         , 4: {'a': 5, 'b': 4, 'c': 3, 'd': 2}}
        PreferenceLists = {1: ['a', 'b', 'c', 'd'],
                  2: ['a', 'b', 'c', 'd'],
                  3: ['a', 'b', 'c', 'd'],
                  4: ['a', 'b', 'c', 'd']
                  }
        house = {1: 'a',
                 2: 'b',
                 3: 'c',
                 4: 'd'}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'a', 2: 'b', 3: 'c', 4: 'd'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'a', 2: 'b', 3: 'c', 4: 'd'})

        PreferenceListsValues = {1: {'a': 5}, 2: {'b': 4}, 3: {'c': 3}, 4: {'d': 2}}
        PreferenceLists = {1: ['a'],
                  2: ['b'],
                  3: ['c'],
                  4: ['d']
                  }
        house = {1: 'a',
                 2: 'b',
                 3: 'c',
                 4: 'd'}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'a', 2: 'b', 3: 'c', 4: 'd'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'a', 2: 'b', 3: 'c', 4: 'd'})

        PreferenceListsValues = {1: {'b': 5}, 2: {'a': 4}, 3: {'d': 3}, 4: {'c': 2}}
        PreferenceLists = {1: ['b'],
                  2: ['a'],
                  3: ['d'],
                  4: ['c']
                  }
        house = {1: 'a',
                 2: 'b',
                 3: 'c',
                 4: 'd'}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'b', 2: 'a', 3: 'd', 4: 'c'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'b', 2: 'a', 3: 'd', 4: 'c'})

        PreferenceListsValues = {1: {'a': 5}, 2: {'c': 4}, 3: {'d': 3}, 4: {'b': 2}}
        PreferenceLists = {1: ['a'],
                  2: ['c'],
                  3: ['d'],
                  4: ['b']
                  }
        house = {1: 'a',
                 2: 'b',
                 3: 'c',
                 4: 'd'}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'a', 2: 'c', 3: 'd', 4: 'b'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'a', 2: 'c', 3: 'd', 4: 'b'})

        PreferenceListsValues = {1: {'a': 5, 'c': 5}, 2: {'c': 4}, 3: {'d': 3}, 4: {'b': 2, 'd': 2}}
        PreferenceLists = {1: [{'a', 'c'}],
                  2: ['c'],
                  3: ['d'],
                  4: [{'b', 'd'}]
                  }
        house = {1: 'a',
                 2: 'b',
                 3: 'c',
                 4: 'd'}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'a', 2: 'c', 3: 'd', 4: 'b'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'a', 2: 'c', 3: 'd', 4: 'b'})

        PreferenceListsValues = {1: {'d': 5}, 2: {'c': 4}, 3: {'a': 3}, 4: {'b': 2}}
        PreferenceLists = {1: ['d'],
                  2: ['c'],
                  3: ['a'],
                  4: ['b']
                  }
        house = {1: 'a',
                 2: 'b',
                 3: 'c',
                 4: 'd'}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'd', 2: 'c', 3: 'a', 4: 'b'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'd', 2: 'c', 3: 'a', 4: 'b'})
        # doesn't work.
        # doesn't work 1(a) delete and c don't have node to point.
        # PreferenceLists = {1: [{'a', 'b'}],
        #           2: ['a', 'd'],
        #           3: ['a'],
        #           4: ['b', 'c'],
        #           5: ['d']}
        #
        # house = {1: 'a',
        #          2: 'b',
        #          3: 'c',
        #          4: 'd',
        #          5: 'e'}

        PreferenceListsValues = {1: {'a': 3, 'c': 3}, 2: {'a': 2, 'b': 2, 'd': 2}, 3: {'c': 9, 'e':9}, 4: {'c': 1}, 5: {'a': 5, 'f': 5},6: {'b': 1}}
        PreferenceLists = {1: [{'a', 'c'}],
                  2: [{'a', 'b', 'd'}],
                  3: [{'c', 'e'}],
                  4: ['c'],
                  5: [{'a', 'f'}],
                  6: ['b']}
        house = {1: 'a',
                 2: 'b',
                 3: 'c',
                 4: 'd',
                 5: 'e',
                 6: 'f'}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'a', 2: 'd', 3: 'e', 4: 'c', 5: 'f', 6: 'b'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'a', 2: 'd', 3: 'e', 4: 'c', 5: 'f', 6: 'b'})

        # 2222222222222222222
        # print(printSCCs({1: 'a',
        #                  2: 'b',
        #                  3: 'c',
        #                  4: 'd',
        #                  5: 'e',
        #                  6: 'f'}, {1: {'a': 8, 'c': 8},
        #                   2: {'a': 1, 'b': 1, 'd': 1},
        #                   3: {'c': 1, 'e': 1},
        #                   4: {'c': 4},
        #                   5: {'a': 1, 'f': 1},
        #                   6: {'b': 2}}))

        PreferenceListsValues = {1: {'g': 3, 'c': 3}, 2: {'f': 2, 'g': 2, 'd': 2}, 3: {'b': 9, 'e':9, 'c': 3}, 4: {'e': 1}, 5: {'d': 5},6: {'b': 1, 'f': 0}, 7:{'a':3}}
        PreferenceLists = {1: [{'g', 'c'}],
                  2: [{'f', 'g', 'd'}],
                  3: [{'b', 'e'}, 'c'],
                  4: ['e'],
                  5: ['d'],
                  6: ['b', 'f'],
                  7: ['a']}
        house = {1: 'a',
                 2: 'b',
                 3: 'c',
                 4: 'd',
                 5: 'e',
                 6: 'f',
                 7: 'g'}
        self.assertEqual(work2022.get_all_values(house, PreferenceListsValues), {1: 'g', 2: 'f', 3: 'c', 4: 'e', 5: 'd', 6: 'b', 7: 'a'})
        self.assertEqual(work2022.print_SCCs(house, PreferenceLists), {1: 'g', 2: 'f', 3: 'c', 4: 'e', 5: 'd', 6: 'b', 7: 'a'})

# same 33333333333333 example


        # # check make_graph_begin
        # PreferenceLists = {1: [{'a', 'b', 'c'}],
        #            2: [{'a', 'b', 'c'}],
        #            3: [{'a', 'b', 'c'}]}
        # house = {1: 'a',
        #  2: 'b',
        #  3: 'c'}
        # graph = nx.DiGraph()
        # graph = work2022.make_graph_begin(PreferenceLists, house, graph)
        # self.assertTrue(graph.__eq__({1: {'b': {}, 'a': {}, 'c': {}}, 'b': {2: {}}, 'a': {1: {}}, 'c': {3: {}}, 2: {'b': {}, 'a': {}, 'c': {}}, 3: {'b': {}, 'a': {}, 'c': {}}}))
        #
        #
        # PreferenceLists = {1: ['a', 'b'],
        #            2: ['b', 'a'],
        #            3: ['c']}
        # house = {1: 'a',
        # 2: 'b',
        # 3: 'c'}
        # graph = nx.DiGraph()
        # graph = work2022.make_graph_begin(PreferenceLists, house, graph)
        # self.assertTrue(graph.__eq__({1: {'a': {}}, 'a': {1: {}}, 2: {'b': {}}, 'b': {2: {}}, 3: {'c': {}}, 'c': {3: {}}}))
        # connect_jealous_agents_to_there_best

        PreferenceLists = {1: [{'g', 'c'}],
                          2: [{'f', 'g', 'd'}],
                          3: [{'b', 'e'}, 'c'],
                          4: ['e'],
                          5: ['d'],
                          6: ['b', 'f'],
                          7: ['a']}
        house = {1: 'a',
                         2: 'b',
                         3: 'c',
                         4: 'd',
                         5: 'e',
                         6: 'f',
                         7: 'g'}

        makeGraph = work2022.make_graph_begin({1: [{'a', 'b'}], 2: [{'a', 'b'}]}, {1: 'a', 2: 'b'}, nx.DiGraph())
        graph = nx.DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node('a')
        graph.add_node('b')
        graph.add_edge(1, 'a')
        graph.add_edge(1, 'b')
        graph.add_edge(2, 'a')
        graph.add_edge(2, 'b')
        graph.add_edge('a', 1)
        graph.add_edge('b', 2)
        self.assertTrue(graph.__eq__(makeGraph))

        PreferenceLists = {1: [{'g', 'c'}],
                          2: [{'f', 'g', 'd'}],
                          3: [{'b', 'e'}, 'c'],
                          4: ['e'],
                          5: ['d'],
                          6: ['b', 'f'],
                          7: ['a']}
        house = {1: 'a',
                         2: 'b',
                         3: 'c',
                         4: 'd',
                         5: 'e',
                         6: 'f',
                         7: 'g'}

        makeGraph = work2022.make_graph_begin(PreferenceLists, house,  nx.DiGraph())
        graph = nx.DiGraph()
        for i in range(7):
            graph.add_node(i+1)
        graph.add_edge(1, 'g')
        graph.add_edge(1, 'c')
        graph.add_edge(2, 'f')
        graph.add_edge(2, 'g')
        graph.add_edge(2, 'd')
        graph.add_edge(3, 'b')
        graph.add_edge(3, 'e')
        graph.add_edge(4, 'e')
        graph.add_edge(5, 'd')
        graph.add_edge(6, 'b')
        graph.add_edge(7, 'a')
        graph.add_edge('a', 1)
        graph.add_edge('b', 2)
        graph.add_edge('c', 3)
        graph.add_edge('d', 4)
        graph.add_edge('e', 5)
        graph.add_edge('f', 6)
        graph.add_edge('g', 7)

        self.assertTrue(graph.__eq__(makeGraph))

        graph.remove_node(2)
        graph.remove_node('b')
        newGraph = graph.copy()


        graph = work2022.make_graph(PreferenceLists, newGraph)

        self.assertTrue(graph.__eq__(newGraph))

        graph = work2022.make_graph_begin(PreferenceLists, house, nx.DiGraph())
        work2022.connect_jealous_agents_to_there_best([1, 2, 3, 4, 5, 6, 7], graph)
        self.assertTrue(graph.__eq__({1: {'c': {}}, 'g': {7: {}}, 'c': {3: {}}, 2: {'d': {}}, 'f': {6: {}}, 'd': {4: {}}, 3: {'b': {}}, 'b': {2: {}}, 'e': {5: {}}, 4: {'e': {}}, 5: {'d': {}}, 6: {'b': {}}, 7: {'a': {}}, 'a': {1: {}}}))

        graph = {1: {'c': {}}, 'g': {7: {}}, 'c': {3: {}}, 2: {'d': {}}, 'f': {6: {}}, 'd': {4: {}}, 3: {'b': {}}, 'b': {2: {}}, 'e': {5: {}}, 4: {'e': {}}, 5: {'d': {}}, 6: {'b': {}}, 7: {'a': {}}, 'a': {1: {}}}
        work2022.connect_satisfied_agents_to_there_best(graph, {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g'}, [1, 'a', 2, 'b', 3, 'c', 4, 'd', 5, 'e', 6, 'f', 7, 'g'])
        self.assertTrue(graph.__eq__({1: {'c': {}}, 'g': {7: {}}, 'c': {3: {}}, 2: {'d': {}}, 'f': {6: {}}, 'd': {4: {}}, 3: {'b': {}}, 'b': {2: {}}, 'e': {5: {}}, 4: {'e': {}}, 5: {'d': {}}, 6: {'b': {}}, 7: {'a': {}}, 'a': {1: {}}}))

if __name__ == '__main__':
    unittest.main()