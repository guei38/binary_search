# binay search
# toby's test
import pdb

my_list = [1,2,5,7,11,23,24,25]
new_list = [1]

dupe_list = [1, 1, 3, 5, 6, 7, 7, 8, 10]

def binary_search(sorted_array, value, start=0, end=-1):
    if end == -1:
        end = len(sorted_array)-1

    if value < sorted_array[start]:
        return -1
    elif value > sorted_array[end]:
        return -1

    middle = int((end + start) / 2)

    #pdb.set_trace()
    if sorted_array[middle] == value:
        return middle

    elif value < sorted_array[middle]:
        return binary_search(sorted_array, value, start, middle-1)

    else:
        return binary_search(sorted_array, value, middle+1, end)



#UNIT TEST, a function to test a function.
# you know what the output should be given an input, and you know the output.  so this is a way to automate testing.  unit test every function!
def test_search(expect, actual):
    if expect == actual:
        print ("Pass")
    else:
        print ("Fail, expected ", expect, ", got ", actual)


test_search(4, binary_search(my_list, 11))

test_search(3, binary_search(my_list, 7))

test_search(5, binary_search(my_list, 23))

test_search(-1, binary_search(my_list, 555))

test_search(0, binary_search(new_list, 1))
test_search(-1, binary_search(new_list, 5))

test_search(6, binary_search(dupe_list, 7))
test_search(1, binary_search(dupe_list, 1))

