n=int(input("Enter a no.:"))
a=1
count=0
while a<=n:
    if n%a==0:
        print(a,"is a factor of",n)
        count=count+1
    a=a+1
print("There are",count,"factors of",n)

    
