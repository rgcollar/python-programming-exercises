# 1) Find if a number is a power of 2:
# Given N integers, for each integer print POWER if it's a power of 2. 
# Otherwise just print the number.

def is_power_of_2(n):
    if n == 1:
        return True
    elif n % 2 == 0:
        return is_power_of_2(n // 2)
    else:
        return False


l_ints = list(range(1, int(input('Please enter a number: '))))

for number in l_ints:
    if is_power_of_2(number):
        print(f"{number} is a power of 2")
    else:
        print(f"{number} is not a power of 2")
