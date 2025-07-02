age=int(input("Enter your age: "))

if age > 0 and age < 13: 
    print("You are a child")

elif age >= 13 and age < 18: 
    print("You are a teenager")

elif age  >= 18 and age < 65:
    print("You are an adult")

elif age >= 65:
    print("You are an elderly")

else: 
    print("Invalid age")


