# code your iterative algorithm here

def binary_search(data, el):
    first = 0
    last = len(data)-1
    found = False

    while first <= last and not found:
        mid = (first+last)//2

        if data[mid] == el:
            found == True