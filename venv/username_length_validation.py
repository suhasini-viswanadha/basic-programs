"""check the length of a username.
      length should be between 8 -32"""

username=input("Enter a username")
b=len(username)

if(b>=8) and (b<=32):
    print("username length looks good",b)

if(b<8) or (b>32):
    print("Length doesnt match...it has to be more than 8 characters and less than 32")

if not((b>=8) and (b<=32)):
    print("Length doesnt match...it has to be more than 8 characters and less than 32")

