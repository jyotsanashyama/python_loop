#Enter a number and identify whether it is palindrome or not.
n=int(input("Enter a no.:"))
n1=n2=n
count=0
temp=0
ans=0
while n!=0:
    n=n//10
    count=count+1
#print("count=",count)
count=count-1
while n1!=0:
    temp=n1%10
    n1=n1//10
    ans=ans+(10**count)*temp
    count=count-1
    #print("ans=",ans)

if ans==n2:
    print("The input number is palindrome no.")
else:
    print("The input number is not palindrome no.")
