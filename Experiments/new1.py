# Function to compute GCD of two numbers

def gcd(a, b):

    while b:

        a, b = b, a % b

    return a

# Function to compute LCM using the GCD
def lcm(a, b):

    return abs(a * b) // gcd(a, b)

# Function to compute LCM of a list of numbers
def lcm_of_list(numbers):

    result = 1

    for num in numbers:

        result = lcm(result, num)

    return result

# Example usage
N = int(input("Enter the No: "))

numbers = list(range(1, N + 1))  # List from 1 to N

result = lcm_of_list(numbers)

print("Minimum number of candies:", result)
