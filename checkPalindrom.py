def is_palindrome(input_string):
    # First, we'll use the rev() function from the previous example to reverse the input string
    reversed_string = rev(input_string)
    # Then we'll compare the reversed string to the original string
    return reversed_string == input_string

# Test the function with a few test cases
print(is_palindrome("racecar")) # True
print(is_palindrome("hello")) # False
print(is_palindrome("a")) # True
