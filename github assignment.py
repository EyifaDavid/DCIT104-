# DCIT 104 GITHUB ASSIGNMENT
# INDEX NUMBER: 10978392
# PRIME NUMBERS LESS THAN A GIVEN NUMBER

import time
import math

def is_prime(n):
  if n>1:
    for i in range (2, int(math.sqrt(n)) + 1):
      if (n % i) == 0:
        return False
    else:
      return True
  else:
    return False

n = int(input("Enter the range"))

start = time.time()

total = 2

i = 3

while i < n:
    if is_prime(i):
        total += i
    i += 2

print(total)


end = time.time()
print(end -start)

