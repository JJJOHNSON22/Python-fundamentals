# 1) Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
#Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(num_list):
    count = 0
    for x in num_list:
        if (x < 0):
            num_list[count] = "big"
            count += 1
        else:
            count += 1
    return num_list

output = biggie_size([5,-2,-4,1,9])
print(output)          

# 2) Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
#Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
#Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_positives(num_list):
    count = 0
    positive_number_count = 0
    for x in num_list:
        while (count < len(num_list) - 1):
            if (x > 0):
                positive_number_count += 1
                count += 1
                break
            else:
                count += 1
                break
    num_list[len(num_list) - 1] = positive_number_count
    return num_list

output1 = count_positives([2,-3,9,4,-2,-8])
output2 = count_positives([8,7,6,-2])
print(output1)
print(output2)

# 3) Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
#Example: sum_total([1,2,3,4]) should return 10
#Example: sum_total([6,3,-2]) should return 7
def sum_total(num_list):
    num_sum = 0
    for x in num_list:
        num_sum += x
    return num_sum

output = sum_total([4,-9,3,6])
print(output)

# 4) Average - Create a function that takes a list and returns the average of all the values.x
#Example: average([1,2,3,4]) should return 2.5
def list_average(num_list):
    num_sum = 0
    for x in num_list:
        num_sum += x
    avg = num_sum / len(num_list)
    return avg

output = list_average([5,3,4,9,2])
print(output)

# 5) Length - Create a function that takes a list and returns the length of the list.
#Example: length([37,2,1,-9]) should return 4
#Example: length([]) should return 0
def give_length(num_list):
    length = 0
    for x in num_list:
        length += 1
    return length

output = give_length([1,6,-3,0])
print(output)

# 6) Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
#Example: minimum([37,2,1,-9]) should return -9
#Example: minimum([]) should return False
def find_minimum(num_list):
    if (num_list == []):
        return False
    min_num = num_list[0]
    for x in num_list:
        if (x < min_num):
            min_num = x
    return min_num

output1 = find_minimum([22,9,-3,7,19])
output2 = find_minimum([])
print(output1)
print(output2)

# 7) Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
#Example: maximum([37,2,1,-9]) should return 37
#Example: maximum([]) should return False
def find_maximum(num_list):
    if (num_list == []):
        return False
    max_num = num_list[0]
    for x in num_list:
        if (x > max_num):
            max_num = x
    return max_num

output1 = find_maximum([5,9,-4,17,3])
output2 = find_maximum([])
print(output1)
print(output2)

# 8) Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
#Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(num_list):
    sum_total = 0
    for x in num_list:
        sum_total += x

    numdict = {
        'sumTotal': sum_total,
        'average': sum_total / len(num_list),
        'minimum': min(num_list, key=lambda key: [key]),
        'maximum': max(num_list, key=lambda key: [key]),
        'length': len(num_list)
    }
    return numdict
print(ultimate_analysis([52,13,9,-22]))

# 9) Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
#Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(num_list):
    temp = 0
    count = 0
    for x in num_list:
        if (len(num_list) // 2 > count):
            temp = num_list[len(num_list) - 1 - count]
            num_list[len(num_list) - 1 - count] = x
            num_list[0 + count] = temp
            count += 1
    return num_list

print(reverse_list([1,2,3,4]))
print(reverse_list([1,2,3,4,5]))