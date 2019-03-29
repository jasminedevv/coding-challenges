'''
Given a matrix that looks something like this:
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

And looking at every 'hourglass' in it which looks like this:

0 0 0
  0 
0 0 0

Tell me which hourglass is the biggest in the array. This is to say sum all the numbers in each hourglass and return the largest.
'''

box = """
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
"""

box2 = """
1 1 1 5 -2 0
2 1 0 0 1 0
1 1 1 5 11 9
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
"""

tbt = [
    [1,1,1],
    [0,1,0],
    [1,1,1]
]
tbt1 = [
    [1,1,1],
    [2,1,2],
    [1,1,1]
]

def parse_box(box):
    """Takes a box as a string and returns an array or arrays where each row is its own array"""
    # lets assume I already wrote this
    return [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]

def sum_hourglass(matrix):
    pass

