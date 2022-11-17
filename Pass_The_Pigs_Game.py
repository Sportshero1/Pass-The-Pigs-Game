import random

# selection for the users
selection = ["Pig with no dot", "Pig with one dot", "Standing Pig", "Pig on Back", "Pig on Snout", "Pig Leaning on Ear"]


#User Selections
user_selection = ["Yes", "No"]

# Point values
# "Pig out"  = 0
# Sider = 1
# Trotter = 5
# Razorback = 5
# Snouter = 10
# "Leaning Jowler" = 15

# Point values determined by rolls
# roll_value =


# Establish Players
num_players = input("1 or 2 players? ")
print()
while num_players != "Goodbye":
    if num_players == "1":
        print("Only 1 player? Have fun!")
        print()
        break
    elif num_players == "2":
        print("May the best roller win!")
        print()
        break
    else:
        print("Invalid response. Try again")
        num_players = "Goodbye"
        

# Create random roll for the two pigs
Pig_Roll_1 = random.choice(selection)
Pig_Roll_2 = random.choice(selection)

# print the results of the rolls
print(f"\nYou rolled {Pig_Roll_1}, & {Pig_Roll_2}")
print()

# check the logic of the rolls
# Pig with no dot
Roll_value = 0

# while Roll_value <= 100:
if Pig_Roll_1 == "Pig with no dot":
    # Assigning outcomes for what happens with the second pig
    if Pig_Roll_2 == "Pig with no dot":
        print("You rolled a Sider! You get one point!")
        Roll_value += 1
    elif Pig_Roll_2 == "Pig with one dot":
        print("You rolled a Pig out! Next Players turn!")
        Roll_value = 0
    elif Pig_Roll_2 == "Standing Pig":
        print("You rolled a Trotter with a Sider! You get five points!")
        Roll_value += 5
    elif Pig_Roll_2 == "Pig on Back":
        print("You rolled a Razorback with a Sider! You get five points!")
        Roll_value += 5
    elif Pig_Roll_2 == "Pig on Snout":
        print("You rolled a Snouter with a Sider! You get ten points!")
        Roll_value += 10
    else:
        print("You rolled a Leaner with a Sider! You get fifteen points!")
        Roll_value += 15
    input("You have a total of {Roll_value} points! Do you want to roll again? Yes or No? ")
    print()
    # while user_selection == "Yes":
    #     continue
    # else:
    #     print("End of turn, Next player Rolls")
# Pig with dot
elif Pig_Roll_1 == "Pig with one dot":
    # Assigning outcomes for what happens with the second pig
    if Pig_Roll_2 == "Pig with dot":
        print("You rolled a Sider! You get one point!")
        Roll_value += 1
    elif Pig_Roll_2 == "Pig with no dot":
        print("You rolled a Pig out! Next Players turn!")
        Roll_value = 0
    elif Pig_Roll_2 == "Standing Pig":
        print("You rolled a Trotter with a Sider! You get five points!")
        Roll_value += 5
    elif Pig_Roll_2 == "Pig on Back":
        print("You rolled a Razorback with a Sider! You get five points!")
        Roll_value += 5
    elif Pig_Roll_2 == "Pig on Snout":
        print("You rolled a Snouter with a Sider! You get ten points!")
        Roll_value += 10
    else:
        print("You rolled a Leaner with a Sider! You get fifteen points!")
        Roll_value += 15
    input("You have a total of {Roll_value} points! Do you want to roll again? Yes or No? ")
    print()
    # while user_selection == "Yes":
    #     continue
    # else:
    #     print("End of turn, Next player Rolls")
# Standing Pig
elif Pig_Roll_1 == "Standing Pig":
    # Assigning outcomes for what happens with the second pig
    if Pig_Roll_2 == "Pig with one dot":
        print("You rolled a Sider with a Trotter! You get five points!")
        Roll_value += 5
    elif Pig_Roll_2 == "Pig with no dot":
        print("You rolled a Sider with a Trotter! You get five points!")
        Roll_value = 5
    elif Pig_Roll_2 == "Standing Pig":
        print("You rolled a Double Trotter! You get twenty points!")
        Roll_value += 20
    elif Pig_Roll_2 == "Pig on Back":
        print("You rolled a Mixed Combo! You get ten points!")
        Roll_value += 10
    elif Pig_Roll_2 == "Pig on Snout":
        print("You rolled a Mixed Combo! You get fifteen points!")
        Roll_value += 15
    else:
        print("You rolled a Mixed Combo! You get twenty points!")
        Roll_value += 20
    input("You have a total of {Roll_value} points! Do you want to roll again? Yes or No? ")
    print()
    # while user_selection == "Yes":
    #     continue
    # else:
    #     print("End of turn, Next player Rolls")
# Pig on Back
elif Pig_Roll_1 == "Pig on Back":
    # Assigning outcomes for what happens with the second pig
    if Pig_Roll_2 == "Pig with one dot":
        print("You rolled a Sider with a Razorback! You get five points!")
        Roll_value += 5
    elif Pig_Roll_2 == "Pig with no dot":
        print("You rolled a Sider with a Razorback! You get five points!")
        Roll_value = 5
    elif Pig_Roll_2 == "Standing Pig":
        print("You rolled a Mixed Combo! You get ten points!")
        Roll_value += 10
    elif Pig_Roll_2 == "Pig on Back":
        print("You rolled a Double Razorback! You get twenty points!")
        Roll_value += 20
    elif Pig_Roll_2 == "Pig on Snout":
        print("You rolled a Mixed Combo! You get fifteen points!")
        Roll_value += 15
    else:
        print("You rolled a Mixed Combo! You get twenty points!")
        Roll_value += 20
    input("You have a total of {Roll_value} points! Do you want to roll again? Yes or No? ")
    print()
    # while user_selection == "Yes":
    #     continue
    # else:
    #     print("End of turn, Next player Rolls")
# Pig on Snout
elif Pig_Roll_1 == "Pig on Snout":
    # Assigning outcomes for what happens with the second pig
    if Pig_Roll_2 == "Pig with one dot":
        print("You rolled a Sider with a Snouter! You get ten points!")
        Roll_value += 10
    elif Pig_Roll_2 == "Pig with no dot":
        print("You rolled a Sider with a Trotter! You get ten points!")
        Roll_value = 10
    elif Pig_Roll_2 == "Standing Pig":
        print("You rolled a Mixed Combo! You get fifteen points!")
        Roll_value += 15
    elif Pig_Roll_2 == "Pig on Back":
        print("You rolled a Mixed Combo! You get fifteen points!")
        Roll_value += 15
    elif Pig_Roll_2 == "Pig on Snout":
        print("You rolled a Double Snouter! You get forty points!")
        Roll_value += 40
    else:
        print("You rolled a Mixed Combo! You get twenty-five points!")
        Roll_value += 25
    input("You have a total of {Roll_value} points! Do you want to roll again? Yes or No? ")
    print()
    # while user_selection == "Yes":
    #     continue
    # else:
    #     print("End of turn, Next player Rolls")
# Pig Leaning on Ear
elif Pig_Roll_1 == "Pig Leaning on Ear":
    # Assigning outcomes for what happens with the second pig
    if Pig_Roll_2 == "Pig with one dot":
        print("You rolled a Sider with a Leaner! You get fifteen points!")
        Roll_value += 15
    elif Pig_Roll_2 == "Pig with no dot":
        print("You rolled a Sider with a Leaner! You get fifteen points!")
        Roll_value = 15
    elif Pig_Roll_2 == "Standing Pig":
        print("You rolled a Mixed Combo! You get twenty points!")
        Roll_value += 20
    elif Pig_Roll_2 == "Pig on Back":
        print("You rolled a Mixed Combo! You get twenty points!")
        Roll_value += 20
    elif Pig_Roll_2 == "Pig on Snout":
        print("You rolled a Mixed Combo! You get twenty-five points!")
        Roll_value += 25
    else:
        print("You rolled a Double Leaning Jowler! You get sixty points!")
        Roll_value += 60
    input("You have a total of {Roll_value} points! Do you want to roll again? Yes or No? ")
    print()
    # while user_selection == "Yes":
    #     continue
    # else:
    #     print("End of turn, Next player Rolls")
# else:
#     print("Congrats on reaching 100 Points")
