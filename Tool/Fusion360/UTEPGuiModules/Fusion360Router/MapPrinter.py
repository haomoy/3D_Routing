'''
Created on Feb 27, 2018

@author: Carlos
'''

def printMap(Map):
    """Print Map given in console.

    Map -- must be list (Two-dimensional) type
    """

    # Print column number line
    print(' =  ', end='')
    for i in range(0, len(Map)):
        if i < 10:
            print ('  ' + str(i), end='')
        else:
            print(' '+str(i), end='')
    print()

    # Print extra line
    for i in range(0, len(Map) + 2):
        print ("  ", end='')
    print()

    # Print Map with row number
    for x in range(len(Map[0])):
        if x < 10:
            print (' ' + str(x) + '  ', end='')
        else:
            print (str(x) + '  ', end='')
        for y in range(len(Map)):
            if len(Map[y][x]) == 1:
                space = '  '
            elif len(Map[y][x]) == 2:
                space = ' '
            else:
                space = ''
            print (space + Map[y][x], end='')
        print()
        
def printMapFile(Amap, outputFile):
    """Print Map given in console.

    Map -- must be list (Two-dimensional) type
    """
    file_handler = open(outputFile, "w+")

    # Print Map with row number
    for x in range(len(Amap[0])):
        for y in range(len(Amap)):
            if len(Amap[y][x]) == 1:
                space = '   '
            elif len(Amap[y][x]) == 0:
                space = '    '
            elif len(Amap[y][x]) == 2:
                space = '  '
            elif len(Amap[y][x]) == 3:
                space = ' '
            else:
                space = ''
            file_handler.write(space + Amap[y][x])
        file_handler.write("\n")
        
def printMapLog(Amap, f):
    """Print Map given in console.

    Map -- must be list (Two-dimensional) type
    """

    # Print Map with row number
    for x in range(len(Amap[0])):
        for y in range(len(Amap)):
            if len(Amap[y][x]) == 1:
                space = '   '
            elif len(Amap[y][x]) == 0:
                space = '    '
            elif len(Amap[y][x]) == 2:
                space = '  '
            elif len(Amap[y][x]) == 3:
                space = ' '
            else:
                space = ''
            f.write(space + Amap[y][x])
        f.write("\n")
    
    