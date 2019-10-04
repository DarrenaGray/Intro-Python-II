from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

player = Player('Player', room['outside'])
print(player)

# Will try to refactor later to make it DRY
while True:
    # print(player.current_room)

    command = input('Press [n], [s], [e], [w] to move. Press [q] to quit: ')

    moves = ['n', 's', 'e', 'w']

    if command == 'q':
        print("Player has exited the game.")
        break

    if command in moves:

        if command == 'n':
            if player.current_room.n_to != None:
                player.current_room = player.current_room.n_to

            else:
                print("There is no room here!")

        elif command == 's':
            if player.current_room.s_to != None:
                player.current_room = player.current_room.s_to

            else:
                print("There is no room here!")

        elif command == 'e':
            if player.current_room.e_to != None:
                player.current_room = player.current_room.e_to

            else:
                print("There is no room here!")
        elif command == 'w':
            if player.current_room.w_to != None:
                player.current_room = player.current_room.w_to

            else:
                print("There is no room here!")

        print(player)

# Old Code

# #
# # Main
# #

# # Make a new player object that is currently in the 'outside' room.
# player = Player("Player", room['outside'])

# # Write a loop that:
# while True:
#     # * Prints the current room name
#     print(player.current_room)
# # * Prints the current description (the textwrap module might be useful here).
# # * Waits for user input and decides what to do.
#     direction = input(
#         "Press to move 'n', 's', 'e', 'w'. Press to exit 'q': ")
# #
#     movements = ['n', 's', 'e', 'w', 'q']
# # If the user enters a cardinal direction, attempt to move to the room there.
#     if direction in movements and player.current_room is not None:
#         if direction == 'n':
#             player.current_room = player.current_room.n_to

#         elif direction == 's':
#             player.current_room = player.current_room.s_to

#         elif direction == 'e':
#             player.current_room = player.current_room.e_to

#         elif direction == 'w':
#             player.current_room = player.current_room.w_to

#     # Print an error message if the movement isn't allowed.
#     else:
#             # print('That is not a valid movement.')
#             print('This way is blocked! Try another direction.')

#     # if player.current_room is None:
#     #     print('This way is blocked! Try another direction.')
#     #     player.current_room

#     # If the user enters "q", quit the game
#     if direction == 'q':
#         print("Player has quit the game")
#         break

# print(player)
