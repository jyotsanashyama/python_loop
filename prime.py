#prime between 1 to n:
n1=int(input("Enter a no.:"))
n = 1
while n<=n1:
    count = 0
    a = 1
    if n==1:
        print(n,"is neither prime nor composite.")
    else:
        while n>=a:
            if n%a==0:
                count=count+1
            a=a+1
        if count==2:
            print(n,"is a prime.")
        else:
            print(n,"is a composite.")
    n = n + 1




