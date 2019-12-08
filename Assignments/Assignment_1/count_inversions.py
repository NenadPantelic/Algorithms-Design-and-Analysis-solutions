counter = 0
def read_file(file):
    file = open(file, 'r')
    nums = list(map(int, file.readlines()))
    file.close()
    return nums


def sort(array):
    if len(array) <= 1:
        return array
    left_array = sort(array[:len(array) // 2])
    right_array = sort(array[len(array) // 2:])
    return merge_and_count_inversions(left_array, right_array)


def merge_and_count_inversions(left_array, right_array):
    merged_array = []
    i = j = 0
    #counter = 0
    global counter
    len_left = len(left_array)
    len_right = len(right_array)
    while i < len_left and j < len_right:
        if left_array[i] < right_array[j]:
            merged_array.append(left_array[i])
            i += 1
        else:
            merged_array.append(right_array[j])
            j += 1
            counter += len_left - i
    while i < len_left:
        merged_array.append(left_array[i])
        i += 1
    while j < len_right:
        merged_array.append(right_array[j])
        j += 1
    #print(counter)
    return merged_array
#array = read_file('test_2.txt')

#print(count_inversions([1,3,5],[2,4,6]))
#print(count_inversions([4,5,6],[1,2,3]))

#print(sort([1,3,5,2,4,6]))
#print(sort(array))
array = read_file('IntegerArray.txt')

sort(array)
f = open('output.txt', 'w')
f.write(str(counter))
f.close()
