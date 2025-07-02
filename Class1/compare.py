years=int(input("Enter the number of years: "))
choice=input("""
Select an option:
1. Calculate days
2. Calculate weeks
3. Calculate hours
 """)


if choice == "1":
    print(f"In {years} years there are {years*365} days")

elif choice == "2":
    print(f"In {years} years there are {years*52} weeks")

elif choice == "3":
    print(f"In {years} years there are {365*years*24} hours")

else:
    print("Invalid choice")