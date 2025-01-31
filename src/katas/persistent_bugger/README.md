# The Persistent Bugger
Write a function, persistence, that takes a **positive integer** `n` as input and returns its **multiplicative persistence**, which is the number of times you must multiply the digits in n until you reach a single-digit number.


```
persistence(39)  # returns 3
# Step 1: 3 * 9 = 27
# Step 2: 2 * 7 = 14
# Step 3: 1 * 4 = 4 (single-digit reached after 3 steps)

persistence(4)   # returns 0
# 4 is already a single-digit number

persistence(25)  # returns 2
# Step 1: 2 * 5 = 10
# Step 2: 1 * 0 = 0 (single-digit reached after 2 steps)
```

**Requirements:**

- If n is already a single-digit number, return 0.
- Use a loop or recursion to calculate the persistence.
- You may use Python's built-in functions like str() to manipulate the digits, but try to keep your solution clean and efficient.