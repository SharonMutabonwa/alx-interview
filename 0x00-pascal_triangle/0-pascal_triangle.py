def pascal_triangle(n):
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
