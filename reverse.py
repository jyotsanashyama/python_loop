#Enter a 4-digit number and print its reverse.
n=int(input("Enter a no.(4-digit):"))
a=3
temp=0
ans=0
while a>=0:
    temp=n%10
    n=n//10
    ans=ans+(10**a)*temp
    #print("temp=",temp)
    #print("n=",n)
    #print("ans=",ans)
    a=a-1
print("The reverse no.=",ans)





