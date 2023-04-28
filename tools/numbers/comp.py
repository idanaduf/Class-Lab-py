#sumofdigits – gets a number and returns sum of digits 
# need to fix VelueError here
def sum_of_digits(num):
    digits_sum = 0
    for digit in str(num): 
      digits_sum += int(digit)      
    return digits_sum


#ispal – return True if the number is palindrome
def ispal(num):
    res = str(num) == str(num)[::-1]
    return res 