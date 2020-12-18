"""this program is to show the use of logical and or operators
    by passing values thru command line"""

import sys
f=sys.argv[0]
a=sys.argv[1]

a=int(a)


if(a%3==0) and (a%5==0):
    print("a is divisible by both 3 and 5")

if (a%3==0) or (a%5==0):
    print("a is divisible by either 3 or 5")
print("testing logical and or operators thru command line")