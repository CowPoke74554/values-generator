#Field of study random generator script
#written by CowPoke74554
#Bachelors of Technology Student (Software Development)
#Oklahoma State University Institute of Technology
#No License
#Code begins on line 8.

import random
# Read values from the file
with open("values.txt", "r", encoding="utf-8") as file:
values = [line.strip() for line in file if line.strip()]
# Ensure there are at least 6 values available
if len(values) < 6:
print("Error: values.txt must contain at least 6 values.")
else:
# Randomly select 6 unique values (no repeats)
selection = random.sample(values, 6)
print("Selected values:")
for value in selection:
print(value)
