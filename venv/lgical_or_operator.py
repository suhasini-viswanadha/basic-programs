pwd=1234
pin=5678
p=1234
i=567

if (pwd==p) or (pin==i):
    print("Authenticated")

if (pwd==p) and (pin!=i):
    print("Sorry you are not authenticated")
