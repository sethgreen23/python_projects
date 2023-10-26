
ordered_list = [1,2,3,4,5,6,7,8,9,10]

def binary_search(ord_list, start, end, element):
    if (start > end):
        print(f'The element {element} doesn\'t exist in the list {ord_list}')
        return
    middle = (end + start) // 2
    if (ord_list[middle] > element):
        binary_search(ord_list, start, middle - 1, element)
    elif (ord_list[middle] < element):
        binary_search(ord_list, middle + 1, end, element)
    else:
        print(f'{element} exist at position {middle}')

binary_search(ordered_list, 0, len(ordered_list) - 1, 15)
