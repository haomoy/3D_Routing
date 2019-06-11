# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 15:47:51 2018

@author: cdtafoya
"""

def BubbleFillMap(Map, center):
    
    """ Perform wave propagation to fill the inside of shapes with fill character.

    Map -- type must be list (Two-dimensional).

    Map -- filled map
    """
    empty_char = 'e'
    fill_char = '-'

    temp = []
    workingPoints = []
    workingPoints.append(center)

    while True:

        for each in workingPoints:

            directions = []
            directions.append((each[0], each[1] - 1))  # above
            directions.append((each[0], each[1] + 1))  # below
            directions.append((each[0] + 1, each[1]))  # right
            directions.append((each[0] - 1, each[1]))  # left

            for dir in directions:

                x = dir[0]
                y = dir[1]

                if x < 0 or x > len(Map) - 1:
                    continue
                if y < 0 or y > len(Map[0]) - 1:
                    continue

                if Map[x][y] == empty_char:
                    Map[x][y] = fill_char
                    temp.append(dir)

        # =======================================================================
        # Here, if temp is empty, it means there are no more workingpoints
        # which means there is nowhere else to go and no path has been found.
        # =======================================================================
        if len(temp) == 0:
            return Map
        workingPoints = temp
        temp = []

    return Map