#Enter a number and count its digits.
n=int(input("Enter a no.:"))
count=0
a=0
ans=0
while n!=0:
    n=n//10
    count=count+1
print("Total no. of digits in the number=",count)


