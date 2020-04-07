import math
n=int(input("Enter a no.:"))
a=2
count=0
temp=int(math.sqrt(n))
#print(temp)
if n==1:
    print(n,"is neither prime nor composite")
else:
    while temp>a:
        if n%a==0:
            count=count+1
            break
        a=a+1
#print(count)
    if count==0:
        print(n,"is a prime no.")
    else:
        print(n,"is a composite no.")
