import decimal
import math

x = 100
z = 10**70  # Using a more manageable representation for your large number

# Method 1: Using the decimal module
print("Using Decimal Module:")
x = 100
# set precision, higher number is more precise but slower
decimal.getcontext().prec = 100
total_decimal = decimal.Decimal(1.0)  # initialize it to 1
while x < z and x < 10**10:  # added a check to stop it from taking forever
    q_decimal = decimal.Decimal(x + 4) / decimal.Decimal(x + 2)
    total_decimal = q_decimal**(decimal.Decimal(x)/4)
    print(x, total_decimal)
    x *= 2

# Method 2: Using logarithms
print("\nUsing Logarithms:")
x = 100
total_log = 0  # Initialize as a sum of logarithms
while x < z and x < 10**10:  # added a check to stop it from taking forever
    q = (x + 4) / (x + 2)
    total_log += (x / 4) * math.log(q)  # Accumulate the log
    total = math.exp(total_log)  # Get the final result
    print(x, total)
    x *= 2
