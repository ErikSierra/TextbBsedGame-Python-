# Project 2
# Erik Sierra
# IT140
# 12/11/22
#
#
#
# create dictionary
rooms = {
    'Lobby': {'South': 'Dining room', 'North': 'Rest area', 'East': 'Laundry Room', 'West': 'Kitchen', 'item': ''},
    'Dining room': {'North': 'Lobby', 'East': 'Bathroom', "item": 'Poke 4'},
    'Bathroom': {'West': 'Dining room', 'item': 'Poke 5'},
    'Laundry Room': {'West': 'Lobby', 'North': 'Gym', 'item': 'Poke 6'},
    'Kitchen': {'East': 'Lobby', 'item': 'Poke 3'},
    'Rest area': {'South': 'Lobby', 'East': 'Storage', 'item': 'Poke 2'},
    'Storage': {'West': 'Rest area', 'item': 'Poke 1'},
    'Gym': {'South': 'Laundry Room', 'item': 'Gym leader'}  # villain
}
# assign variables
items = ['Poke 1', 'Poke 2', 'Poke 3', 'Poke 4', 'Poke 5', 'Poke 6']
item_youSee = ''
inventory = []
inventory_blank = []
Valid_moves = ['North', 'East', 'South', 'West']  # Valid moves are presented in list
location = 'Lobby'
x = 0
move_entered = ''
inventory1 = []


# create function to print objective
def objective():  # Function to print story
    print(
        "--------------------------------------------------------------------------------------------------------------------------- \nYou are a Pokémon trainer and accidentally let your Pokémon run away in the "
        "stadium. You need to find and collect your Pokémon in the rooms of the stadium to be able to beat the gym "
        "leader.\nYou won’t be strong enough to beat the gym leader if you don’t have all 6 of your Pokémon. Good "
        "luck! \n "
        "--------------------------------------------------------------------------------------------------------------------------")


# create function to create instructions
def instructions():  # Function to print directions
    print("You can move: North, East, South, West\n --------------------------------------------------------")


# create function to add items to inventory
def add2_inventory():
    global inventory, inventory1
    get_item = input("Do you want to pick up this item? (Yes or No) ")  # ask for input to pickup up item
    if get_item == "Yes":  # if statement based on what happens if yes or no is chosen
        if inventory == inventory_blank:
            inventory.append(item_youSee)
        else:
            inventory.append(item_youSee)
        print("   You picked up ", item_youSee)
    elif get_item == 'No':
        print('   You did not pick anything up')
    else:
        print("! ! ! ! INVALID MOVE ! ! ! ! ")

# creates function to move between rooms
def move_room():
    global location, item_youSee, x
    while move_entered != 'Exit': # creates infinite loop (until broken) to decide what happens when you move a direction
        print("***********************   NOW IN " + location.upper() + "   *****************************")
        print("   Current Inventory: ", inventory)
        possible_moves = rooms[location].keys() # assign the keys/directions from dictionary to "possible moves"
        print("   You can move: ", *possible_moves)  # unpacks variable from above and combines with string statement
        direction = input("Which direction do you want to move? ").strip()
        if direction == 'Exit': # if statement if player wants to quit the game
            print("Boooo, you quit :( Thanks for playing tho!")
            break  # breaks while loop
        elif direction in possible_moves:  # if inputted direction is one of the possible moves, elif statement runs
            print("   You moved: ", direction)
            new_location = rooms[location].__getitem__(direction).split()  # changes location of player based on
                                                                            # inputted location and dictionary
            location = ' '.join(map(str, new_location))
            if rooms[location].__getitem__('item') in items: # if statement to determine if "add2_inventory" function runs to add items to player inventory
                item_youSee = rooms[location].__getitem__('item')
                if item_youSee in inventory:
                    Item_seeninInventory = 'Yes'
                else:
                    Item_seeninInventory = 'No'
                if Item_seeninInventory == 'No':
                    print("   You see: ", item_youSee)
                    add2_inventory()  # calls function (above)
                else:
                    print("No items to pick up")
            if len(inventory) == 0:  # if statement to print what is in inventory based on where player is in game
                print("Inventory: No Pokes found yet!")
            else:
                print('Inventory: ', inventory)
            x = 0
            if location == 'Gym':  # If statement: if location is the gym (final room), either player must have length of 6 elements (pokes) in inventory, or they lose (refer to respective print messages)
                if len(inventory) == 6:
                    print('Alright! You defeated the gym leader! You won the Python Gym Bade!')
                    print('Thanks for playing!')
                    break  # breaks while loop
                else:
                    print("Oh no! You didn't find all your pokemon and weren't strong enough to defeat the gym leader")
                    print(
                        "Hope to see you stronger next time!\n--------------------------------------------------------")
                    break  # breaks while loop
        else:  # if player enters invalid direction
            print("That's a wall\n--------------------------------------------------------")
            print("   You can move: ", *possible_moves)
            x = x + 1  # creates if statements to state consequences of too many incorrect inputs (ends game if => 5)
            if x == 4:
                print("You've attempted too many wrong directions. Only 1 more try before the game ends")
            if x > 4:
                print("Game Over. You took too many tries. Read the directions for how to "
                      "move\n--------------------------------------------------------")
                break  # breaks while loop


objective()  # prints story by calling function
instructions()  # Prints directions by calling function
move_room()  # Calls function to move between rooms
