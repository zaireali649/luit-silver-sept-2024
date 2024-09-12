import random  # Import the random module to generate random numbers

# Generate a random integer between 0 and 10 (inclusive) and assign it to 'number'
number = random.randint(0, 10)

# Print the randomly generated number
print(number)

import uuid  # Import the uuid module

# Generate a random UUID
unique_id = uuid.uuid4()

print(f"Generated Unique ID: {unique_id}")

from datetime import datetime, timedelta  # Import specific classes from datetime

# Get the current date and time
current_time = datetime.now()

# Calculate 7 days from now
future_time = current_time + timedelta(days=7)

print(f"Current Time: {current_time}")
print(f"Future Time (7 days later): {future_time}")

import math  # Import the math module

# Calculate the square root of 16
sqrt_value = math.sqrt(16)

# Calculate the cosine of pi radians
cosine_value = math.cos(math.pi)

print(f"Square Root of 16: {sqrt_value}")
print(f"Cosine of pi: {cosine_value}")
