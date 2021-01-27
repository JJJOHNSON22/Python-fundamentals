## Palindrome Assignment
##Input "a x a"
##Output = true

word1 = "racecar"

def check_palindrome(word):
    for x in range(0, len(word), 1):
        start_palindrome = word[x]
        end_palindrome = word[len(word) - 1 - x]
        mid_point = len(word) // 2
        if (start_palindrome != end_palindrome):
            return False
        elif (x >= mid_point):
            return "True"
        else:
            print("Good")

check_palindrome(word1)
