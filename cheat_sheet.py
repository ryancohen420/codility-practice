# cheat_sheet.py
# ========================
# Python Cheat Sheet
# ========================
#
# A living reference of common syntax, data structures, and idioms.
# Copy this file into your IDE and update it as you learn new patterns.

# ------------------------------------------------------------------------------
# 1. Variables & Basic Types
# ------------------------------------------------------------------------------
# Integers, floats, strings, booleans
x: int      = 42
pi: float   = 3.14159
name: str   = "Alice"
flag: bool  = True

# Multiple assignment
a, b, c = 1, 2, 3

# ------------------------------------------------------------------------------
# 2. Lists (dynamic arrays)
# ------------------------------------------------------------------------------
# Declaration
my_list: list[int] = [1, 2, 3, 4]

# Indexing & slicing
first_item = my_list[0]
sublist     = my_list[1:3]   # items at positions 1 and 2

# Common methods
my_list.append(5)           # [1,2,3,4,5]
my_list.insert(2, 99)       # insert 99 at index 2
my_list.pop()               # remove & return last element
my_list.remove(99)          # remove first occurrence of 99
length = len(my_list)       # number of elements

# Iteration
for item in my_list:
    print(item)

# ------------------------------------------------------------------------------
# 3. Dictionaries (maps)
# ------------------------------------------------------------------------------
# Declaration
my_dict: dict[str, int] = {"alice": 30, "bob": 25}

# Access & mutation
age_alice = my_dict["alice"]
my_dict["carol"] = 22

# Safe lookup
age_dave = my_dict.get("dave", 0)  # returns 0 if "dave" not found

# Iterate keys, values, items
for key in my_dict:
    print(key, my_dict[key])

for key, val in my_dict.items():
    print(key, val)

# ------------------------------------------------------------------------------
# 4. Sets (unique collection)
# ------------------------------------------------------------------------------
# Declaration
my_set: set[int] = {1, 2, 3}

# Add & remove
my_set.add(4)
my_set.remove(2)      # KeyError if 2 not in set
my_set.discard(5)     # No error if 5 not in set

# Membership test (O(1))
if 3 in my_set:
    print("3 is present")

# ------------------------------------------------------------------------------
# 5. Loops & Iteration
# ------------------------------------------------------------------------------
# For-loop with range
for i in range(5):           # 0,1,2,3,4
    print(i)

for i in range(2, 10, 2):     # 2,4,6,8
    print(i)

# Loop over list with index
for idx, val in enumerate(my_list):
    print(f"{idx}: {val}")

# While-loop
count = 0
while count < 3:
    print(count)
    count += 1

# ------------------------------------------------------------------------------
# 6. Functions
# ------------------------------------------------------------------------------
# Definition
def add(a: int, b: int) -> int:
    return a + b

# Default arguments & keyword args
def greet(name: str = "world") -> None:
    print(f"Hello, {name}!")

# Variable-length args
def concat(*words: str) -> str:
    return " ".join(words)

# ------------------------------------------------------------------------------
# 7. List / Set / Dict Comprehensions
# ------------------------------------------------------------------------------
# List comprehension
squares = [x * x for x in range(10) if x % 2 == 0]

# Set comprehension
unique_even = {x for x in range(20) if x % 2 == 0}

# Dict comprehension
square_map = {x: x * x for x in range(5)}

# ------------------------------------------------------------------------------
# 8. String Operations
# ------------------------------------------------------------------------------
s: str = "hello, world"
parts = s.split(",")        # ["hello", " world"]
joined = ",".join(parts)    # "hello, world"
upper = s.upper()           # "HELLO, WORLD"
trim  = s.strip()           # remove whitespace ends

# ------------------------------------------------------------------------------
# 9. File I/O
# ------------------------------------------------------------------------------
# Read entire file
# with open("data.txt", "r") as f:
#     text = f.read()

# Read lines
# with open("data.txt") as f:
#     for line in f:
#         print(line.rstrip())

# Write to file
# with open("output.txt", "w") as f:
#     f.write("Hello\n")

# ------------------------------------------------------------------------------
# 10. Exceptions
# ------------------------------------------------------------------------------
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Cannot divide by zero:", e)
finally:
    print("Cleanup if needed")

# ------------------------------------------------------------------------------
# 11. Common Modules
# ------------------------------------------------------------------------------
# math
import math
print(math.sqrt(16))

# random
import random
print(random.randint(1, 10))

# collections
from collections import defaultdict, Counter
cnt = Counter([1,2,2,3])

# ------------------------------------------------------------------------------
# 12. Testing Snippet
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    # quick sanity checks
    print("add:", add(2, 3))          # 5
    print("concat:", concat("a","b")) # "a b"
    print("squares:", squares)        # [0,4,16,36,64]
