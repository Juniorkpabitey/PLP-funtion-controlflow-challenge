#Create a function named large_power() that takes two parameters named base and exponent.
#If base raised to the exponent is greater than 5000, return True, otherwise return False

def large_power(base, exponent):
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False

# Example usage:
base_value = 10
exponent_value = 10
result = large_power(base_value, exponent_value)
print(result)

