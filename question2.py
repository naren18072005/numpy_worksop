# find if the given number is a palindrome or not?
def is_palindrome(number):
    str_num = str(abs(number))
    reversed_str_num = str_num[::-1]
    return str_num == reversed_str_num


number = -12321
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else
