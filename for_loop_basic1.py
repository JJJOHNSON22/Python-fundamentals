#1) Basic - Print all integers from 0 to 150.
def print_ints():
    for x in range(0, 151, 1):
        print(x)

print_ints()

#2) Multiples of Five - Print all the multiples of 5 from 5 to 1,000
def print_ints_five():
    for x in range(5, 1001, 5):
        print(x)

print_ints_five()

#3) Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
def print_ints_or_string():
    for x in range(1, 101, 1):
        if (x % 10 == 0):
            print("Coding Dojo")
        elif (x % 5 == 0):
            print("Coding")
        else:
            print(x)

print_ints_or_string()

#4) Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
def print_odd_sum():
    sum = 0
    for x in range(0, 500000, 1):
        if (x % 2 != 0):
            sum = sum + x
    return sum

output = print_odd_sum()
print(output)

#5) Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
def countdown_by_fours():
    for x in range(2018, 0, -4):
        print(x)

countdown_by_fours()

#6) Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
def flexible_counter(lowNum, highNum, mult):
    for x in range(lowNum, highNum, 1):
        if (lowNum % 5 == 0):
            print(x)

lowNum = 3
highNum = 25
mult = 4

flexible_counter(lowNum, highNum, mult)