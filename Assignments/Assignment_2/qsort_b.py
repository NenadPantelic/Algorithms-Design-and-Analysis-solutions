
# version 2 - pivot = the last element
num_of_comparisons = 0  

def swap_pivot(array, low, high):
    array[high-1], array[low] = array[low], array[high-1]
  
num_of_comparisons = 0  
def quick_sort(array, low, high):
    global num_of_comparisons
    if low >= high:
        return
    swap_pivot(array, low, high)
    pivot = partition(array, low, high)
    quick_sort(array, low, pivot-1)
    num_of_comparisons += pivot-1-low
    quick_sort(array, pivot, high)
    num_of_comparisons += high - pivot
    


def partition(array, low, high):
    # i - bound between elements less than pivot and elements greater than pivot
    pivot = array[low]
    i = low+1
    # j - bound between checked and unchecked elements
    for j in range(low+1, high):
        if array[j] < pivot:
            array[j], array[i] = array[i], array[j]
            i = i+1
    array[low], array[i-1] = array[i-1], array[low]
    return i


def read_file_to_array(filename):
    file = open(filename, 'r')
    array = list(map(int, file.readlines()))
    return array

array = read_file_to_array('QuickSort.txt')
quick_sort(array, 0, len(array))
print(num_of_comparisons)
# Answer - 164123


