import sys
import os
from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
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


def get_new_player_room(player_input, player):
    if player_input == 'n':
        return player.current_room.n_to
    elif player_input == 'e':
        return player.current_room.e_to
    elif player_input == 's':
        return player.current_room.s_to
    elif player_input == 'w':
        return player.current_room.w_to


def process_input(player_input, player, options):
    if player_input == 'q':
        return {'proceed': False, 'quit': True}
    elif player_input in options:
        return {'proceed': True, 'current_room': get_new_player_room(player_input, player), 'quit': False}
    else:
        return {'proceed': False, 'current_room': player.current_room, 'quit': False}


def get_input_options(player):
    valid_input = []
    if not player.current_room.n_to.does_block:
        valid_input.append('n')
    if not player.current_room.e_to.does_block:
        valid_input.append('e')
    if not player.current_room.s_to.does_block:
        valid_input.append('s')
    if not player.current_room.w_to.does_block:
        valid_input.append('w')

    return valid_input


def get_input_option_string(options):
    option_string = "You can press"

    for option in options:
        if option == 'n':
            option_string = f"{option_string} n to go North or"
        if option == 'e':
            option_string = f"{option_string} e to go East or"
        if option == 's':
            option_string = f"{option_string} s to go South or"
        if option == 'w':
            option_string = f"{option_string} w to go West or"

    return f"{option_string} q to quit.\nWhat do you choose? "


def clear_screen():
    _ = os.system('cls') if sys.platform.startswith('win32') else os.system('clear')


def get_input(message):
    return str.lower(input(message))


def game_loop():
    clear_screen()
    player_name = input("What is your name, brave hero?\n")
    player = Player(player_name, room['outside'])

    while True:
        clear_screen()

        options = get_input_options(player)
        input_option_string = get_input_option_string(options)
        print(
            f"[|{player.current_room.name}|]\n\n"
            f"{player.current_room.description}\n\n"
        )

        player_input = get_input(input_option_string)
        input_results = process_input(player_input, player, options)

        while not input_results['proceed'] and not input_results['quit']:
            message = "\nThat was an invalid option\n"
            player_input = get_input(f"{message}{input_option_string}")
            input_results = process_input(player_input, player, options)

        if input_results['quit']:
            clear_screen()
            return

        player.current_room = input_results['current_room']


if __name__ == '__main__':
    game_loop()
