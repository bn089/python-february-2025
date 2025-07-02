# tip=int(input("How much would you like to tip?: "))

choice=int(input("""
Select an option:
1. Standard tip 15%
2. Good tip 18%
3. Great tip 20%
4. Hero tip more than 20%
"""))

if choice == 1:
    print("Standard tip is 15%")
    
elif choice == 2: 
    print("Good tip is 18%")

elif choice == 3:
    print("Great tip is 20%")

elif choice == 4: 
    tip=int(input("How much would you like to tip?: "))
    if tip > 20:
        print("My hero")
    else:
        print("Please enter a valid tip percentage")
