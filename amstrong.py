def is_armstrong(num):
    # Convert number to string to easily access digits
    num_str = str(num)
    num_digits = len(num_str)
    
    # Calculate the sum of digits raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum of powers equals the original number
    return sum_of_powers == num

# Test examples
print(is_armstrong(153))  # True, because 1^3 + 5^3 + 3^3 = 153
print(is_armstrong(9474)) # True, because 9^4 + 4^4 + 7^4 + 4^4 = 9474
print(is_armstrong(370))  # True, because 3^3 + 7^3 + 0^3 = 370
print(is_armstrong(123))  # False, because 1^3 + 2^3 + 3^3 = 36
"""
                    Example Explanation:
                    153 is an Armstrong number because:
                    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

                    9474 is an Armstrong number because:
                    9^4 + 4^4 + 7^4 + 4^4 = 6561 + 256 + 2401 + 256 = 9474

                    370 is an Armstrong number because:
                    3^3 + 7^3 + 0^3 = 27 + 343 + 0 = 370

                    123 is not an Armstrong number because:
                    1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36, which is not equal to 123.

                    -------------------------More Examples of Armstrong Numbers:-------------------------------
                    153:
                    1^3 + 5^3 + 3^3 = 153
                    Armstrong number.

                    370:
                    3^3 + 7^3 + 0^3 = 370
                    Armstrong number.

                    371:
                    3^3 + 7^3 + 1^3 = 371
                    Armstrong number.

                    407:
                    4^3 + 0^3 + 7^3 = 407
                    Armstrong number.

                    Code to Find All Armstrong Numbers in a Range (e.g., 1 to 1000):
"""
def find_armstrong_numbers_in_range(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        if is_armstrong(num):
            armstrong_numbers.append(num)
    return armstrong_numbers

# Find Armstrong numbers between 1 and 1000
print(find_armstrong_numbers_in_range(1, 1000)) #[1, 153, 370, 371, 407]

