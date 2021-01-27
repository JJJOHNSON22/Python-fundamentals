# 1) Countdown - Create a function that accepts a number as an input. 
# Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
#Example: countdown(5) should return [5,4,3,2,1,0]
def countdown(num, arr):
    if (isinstance(num, int) == False):
        return "Not a number"
    elif (num > 0):
        for x in range(num, 0, -1):
            arr.append(x)
    else: 
        for x in range(num, 0, 1):
            arr.append(x)
    return arr

array = []
number = eval(input("Please type in a number: "))
output = countdown(number, array)
print(output)

# 2) Print and Return - Create a function that will receive a list with two numbers.
#  Print the first value and return the second.
#Example: print_and_return([1,2]) should print 1 and return 2
def print_and_return(number_list):
    print(number_list[0])
    return number_list[1]

num_list = [1,2]
output = print_and_return(num_list)
print(output)

# 3) First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
#Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
def first_plus_length(num_list, num_sum):
    for x in num_list:
        num_sum += x
    return num_sum

num_sum = 0
num_list = [1,2,3,4,5]
output = first_plus_length(num_list, num_sum)


# 4) Values Greater than Second - Write a function that accepts
#  a list and creates a new list containing only the values
#  from the original list that are greater than its 2nd value.
#  Print how many values this is and then return the new list.
#  If the list has less than 2 elements, have the function return False
#Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
#Example: values_greater_than_second([3]) should return False
def values_greater_than_second(number_list):
    new_number_list = []
    if (len(number_list) < 2):
        return False
    else:
        for x in number_list:
            if (x > number_list[1]):
                new_number_list.append(x)
    print(len(new_number_list))
    return new_number_list

number_list = [9,3,5,1,7,0,2,6]
output1 = values_greater_than_second(number_list)
number_list = [27]
output2 = values_greater_than_second(number_list)
print(output1)
print(output2)

# 5) This Length, That Value - Write a function that accepts two integers as parameters: size and value. 
# The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
#Example: length_and_value(4,7) should return [7,7,7,7]
#Example: length_and_value(6,2) should return [2,2,2,2,2,2]
def this_length_that_value(size, value):
    count = 0
    num_list = []
    while (count < size):
        num_list.append(value)
        count += 1
    return num_list

output1 = this_length_that_value(2,6)
output2 = this_length_that_value(6,9)
print(output1)
print(output2)

