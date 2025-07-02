food=("burger", "pizza", "pasta", "salad")
drinks=("water", "soda", "juice", "tea")

my_list=list(food) # Convert tuple to list to modify it
my_list.append("sushi")  # Adding a new item to the food tuple
print(my_list) 


print(food)
print(drinks)
print(food[-1])
print(drinks[-2])

print(f"Can I have a {food[0]} and a {drinks[1]}?")