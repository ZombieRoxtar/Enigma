#!/usr/bin/env python3

__author__ = 'Chris Roxby'

## Enigma ##
# This script is designed to encrypt and decrypt text with needing to know which is which
# based on multiple Ceaser Ciphers in the style of the Enigma machine.
# https://en.wikipedia.org/wiki/Enigma_machine
##
# TODO: Possibly add a plugboard, allowing any pair of letters to trade places.
# In practice: Any occurance of the letter will trade places
# with its partner before and after the substitution.

from string import ascii_uppercase as ALPHABET
from collections import deque

##
# Each rotor on the Enigma machine had the alphabet written
# around it. So each would swap one letter for another
# which varied based on how much each rotor was turned.
# Variations on the Enigma machine had different numbers of rotors.
##
# Enigma rotor settings are quantified here
# by how many positions that rotor would be turned.
# Enter any number of numbers here.
Rotors = (8, 6, 16, -5, 3)

# Returns a Ceaser Cipher with
# the new alpabet shifted by the
# amount the rotor was turned.
def Swap(letter, offset = 1):
    # Only transform letters
    if letter.isalpha():

        # Using a reversed alphabet was actually 
        # key to making the encryption revesible.
        newAlph = deque(ALPHABET[::-1])

        # Apply the specifed rotor shift.
        newAlph.rotate(offset)

        # Count to the position of the 
        # orignal (capital) letter.
        pos = ALPHABET.index(letter.upper())

        # Find the corrosponding letter
        # in the shifted alphabet.
        letter = newAlph[pos]

    # Return the new letter.
    return(letter)
##

# This is the main loop.
def Enigma():
    # Prompt for text.
    message = input("Enter your message.\n")

    # Entering "QUIT" cancels execution and ends the program.
    if message == "QUIT" or message == "quit":
        global Run
        Run = False
        return

    # This will hold the new message
    new_message = ''

    # Parse each character. 
    # The transformation will skip non-letters.
    for letter in message:
        # If more than one rotor was used
        if hasattr(Rotors, "__len__"):
            # "Pass through" each rotor.
            letter = Swap(letter, Rotors[0])
            for num in Rotors:
                if num > 0:
                    # Reflect the position every time
                    # to make encryption revesible.
                    letter = Swap(letter, int(len(ALPHABET)/2))
                    letter = Swap(letter, num)
        else:
            # If only one rotor was used
            # then just do one swap.
            letter = Swap(letter, Rotors)
        # Add the character to the new string.
        new_message += letter

    # Print the new message.
    print(new_message)
##

# This runs the main function unless "QUIT" is entered.
while Run is True:
    Enigma()