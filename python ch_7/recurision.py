def fact(n):
    if (n == 1 or n == 0):
        return 1
    else:
       return  n * fact(n-1)
    
n = int(input("entr the number:"))
print(f"the factorial of {n} = {fact(n)}")
