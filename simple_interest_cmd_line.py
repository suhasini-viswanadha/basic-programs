"""demonstrates how to use command line"""
import sys

f=sys.argv[0]
p=sys.argv[1]
t=sys.argv[2]
r=sys.argv[3]

p=int(p)
t=int(t)
r=float(r)

i=(p*t*r)/100
print(i)