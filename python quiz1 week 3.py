
def large_power(base, exponent):
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False

def divisible_by_ten(num):
    remainder = num % 10
    if remainder == 0:
        return True
    else:
        return False
print(large_power(10, 3))  # Output: True (10^3 = 1000, which is less than 5000)
print(large_power(100, 2)) # Output: True (100^2 = 10000, which is greater than 5000)
print(divisible_by_ten(20)) # Output: True (20 is divisible by 10)
print(divisible_by_ten(25)) # Output: False (25 is not divisible by 10)



