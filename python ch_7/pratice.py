'''def goodday():
    print("Good day")

goodday()    

def great(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))
print(f"the greast of {a},{b},{c} = {great(a,b,c)}")

def f_to_c(f):
    return 5*(f-32)/9

f=int(input("enter the farenheit value:"))
c=f_to_c(f)
print(f"{round(c,2)}celsius")

print("a")
print("b")
print("c",end="")
print("d",end="")


def sum(n):
    if (n == 1):
        return 1
    else:
        return sum(n-1) + n

n = int(input("enter the number:"))
print(sum(n))        


def pat(n):
    if (n==0):
        return
    print("*" * n)
    pat(n-1)


n = int(input("enter the number:"))
pat(n)    


def inchtocm(n):
    return n*2.54

n=int(input("enter the inch value:"))
m = inchtocm(n)
print(f"{m}cm")

def rem(l,word):
    n = []
    for item in l:
        if not (item == word):
            n.append(item.strip(word))
            
    return n
        
l = ["sai","palani","thq","kumar"]
print(rem(l,"a"))        

'''

def mult(n):
    for i in range(1,11):
        print (f"{n} X {i} = {n*i}")
    return "done"
n = int(input("enter the number:"))
print(mult(n))