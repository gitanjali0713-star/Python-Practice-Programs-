name=input("Enter your name :")
science=int(input("Enter your science marks :"))
maths=int(input("Enter your maths marks:"))
social=int(input("Enter your social marks:"))
total=science+maths+social
percentage=total/3

if percentage>=90:
    Grade="O"
elif percentage>=80:
    Grade="A+"        
else:
    Grade="A"

print("\nStudent Name:",name)
print("Total Marks:",total)                                                     
print("Percentage:",percentage)
print("Grade:",Grade)