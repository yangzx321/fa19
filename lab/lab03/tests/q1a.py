test = {   'name': 'q1a',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> squared_loss(2, 1)\n1',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> squared_loss(2, 0)\n4',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> squared_loss(5, 1)\n16',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'np.sum((squared_loss(np.array([5, '
                                               '6]), np.array([1, 1])) - '
                                               'np.array([16, 25]))**2)\n'
                                               '0',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}