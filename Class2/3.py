# 1 Task: write a program to calculate the sum of numbers from 1 to 100 using for loop:
# sum=0
# for i in range(101):
#     sum+= i
# print(sum)


# #2 Task: create a counter that counts down from 100 to 1, print out the counter:
# for i in range(100, 0, -1):
#     print(i)


# # 3 Task: print the multiplication table of a number given by the user:
# number = int(input("Enter a number: "))
# for hello in range(11):
#     print(f"{number}*{hello}={number * hello}")



# 4 Task: print numbers from 1 to 100 
# for 3, 6, 9, 12, 15 (for every 3rd) add foo
# for 5, 10, 15, 20 (for every 5th) add bar
# for 10, 20, 30 (for every 10th) add hello 


for i in range(1, 101):
    x=str(i)
    
    if i % 3 == 0:
        x += " foo"

    if i % 5 == 0:
        x += " bar"

    if i % 10 == 0:
        x += " hello"
    print(x)