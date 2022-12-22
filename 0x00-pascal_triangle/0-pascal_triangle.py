"""This module represents pascale_triangle function"""


def pascal_triangle(n):
    """Returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    list = [1]
    if (n <= 0):
        return []
    else:
        for i in range(n):
            print(list)
            newlist = []
            newlist.append(list[0])
            for i in range(len(list)-1):
                newlist.append(list[i]+list[i+1])
            newlist.append(list[-1])
            list = newlist
