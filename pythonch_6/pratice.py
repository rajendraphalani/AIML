'''n = int(input("enter the number: "))

for i in range(1,11):
    print(f"{n} X {i} = {n*i}")
    
l = ["sai", "sandeep", "paalani", "data"]

for name in l:
    if(name.startswith("s")):
        print(f"Hello {name}")
        
n = int(input("enter the number: "))
i=1
while(i<=10):
    print(f"{n} X {i} = {n*i}") 
    i += 1
n = int(input("enter the number: "))
for i in range(2,n):
    if (n%i) == 0:
        print("not prime number")
        break
else:
    print("prime number")
    

n = int(input("Enter a number: "))
i = 1
sum = 0
while (i<=n):
    sum += i
    i+=1

print(sum)

n = int(input("Enter a number: "))
p = 1
for i in range(1, n+1):
     p = p * i

print(p)


n = int(input("Enter a number: "))
for i in range(1,n+1):
    print(" "* (n-i),end="")
    print("*"*(2*i-1),end="")
    print("")



n = int(input("Enter a number: "))
for i in range(1,n+1):
    print("*5"* i,end="")
    
    print("")



n = int(input("Enter a number: "))
for i in range(1,n+1):
    if (i==1 or i==n):
        print("*"* n,end="")
    else:
        print("*",end="")
        print(" "* (n-2),end="")
        print("*",end="")  

    print("") 

                                              
'''
n = int(input("Enter a number: " ))
for i in range(1,11):
    print(f"{n} X {11-i} = {n*(11-i)}")
    
