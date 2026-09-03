o=int(input("Enter a first number :"))
p=int(input("Enter second number :"))
q=int(input("Enter a third number:"))
if o>p and o>q:
    greatest=o
elif p>o and p>q:
    greatest=p
else:
    greatest =q

    if o<p and o<q:
        smallest = o
    elif p<o and p<q:
        smallest = p 
    else:
        smallest =q 
print("The greatest number is :",greatest)
print("The smallest number is :",smallest)