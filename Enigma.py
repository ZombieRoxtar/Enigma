#!/usr/bin/env python3

__author__ = 'Chris Roxby'

## Enigma ##
# This script is designed to encrypt and decrypt text with needing to know which is which
# based on multiple Ceaser Ciphers in the style of the Enigma machine.
# https://en.wikipedia.org/wiki/Enigma_machine
##
# TODO: Read settings from INI or similar

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

##
# Enigma machines had a board with plugs
# for each letter. Running a wire from
# one letter to another would cause
# the letters to trade themselves in
# the machine.
# Typically, 10 wires were used.
# The mathematical maximum is 13.
##
# Invalid plugs, such as those that re-use
# a letter will produce results that
# can't be decrypted correctly.
##
# All of these examples are valid.
#Plugs = () # No wires
#Plugs = ('F', 'T') # One wire
Plugs = (('F', 'T'), ('J', 'K')) # Multiple wires
# 13 wires
#Plugs = (('A', 'B'), ('C', 'D'), ('E', 'F'), ('G', 'H'),
#         ('I', 'J'), ('K', 'L'), ('M', 'N'), ('O', 'P'),
#         ('Q', 'R'), ('S', 'T'), ('U', 'V'), ('W', 'X'), ('Y', 'Z'))

Run = True # The program stops when this is false.

# Returns the specified letter's
# partner on the plugboard.
# Returns the letter otherwise.
def Trade(letter):
    # Open each pair in the
    # plugboard settings
    for pairing in Plugs:
    # This will silently fail
    # when Plugs is empty.

        # Python needs to know
        # if the array contains
        # even more arrays.
        if (len(pairing) > 1):
            p0 = pairing[0]
            p1 = pairing[1]
        else:
            p0 = Plugs[0]
            p1 = Plugs[1]
        # This means that the "else"
        # code will run with a
        # one wire setting
        # and the "if" code will run
        # with multiple wires.

        # If the letter in the beginning of the pair
        if (letter.upper() == p0.upper()):
            # Return the other letter.
            return(p1.upper())

        # If the letter in the end of the pair
        if (letter.upper() == p1.upper()):
            # Return the first letter.
            return(p0.upper())

    # If none of that happens just
    # return the input letter.
    return letter
##

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
    return letter
##

# Advance each rotor by one.
def Roll(rotors):
    # Convert to list to
    # allow assignment.
    rotors = list(rotors)

    # Take each rotor number.
    for idx, num in enumerate(rotors):
        # Add 1 to it.
        rotors[idx] += 1

    # Convert back to
    # expected format.
    rotors = tuple(rotors)

    # Return the new position(s).
    return rotors
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

    # Create a copy of the rotors.
    rotors=Rotors
    # These numbers will advance with
    # Each letter, but will be discarded
    # when the output is given.

    # Parse each character.
    # The transformation will skip non-letters.
    for letter in message:

        # Check for plugboard
        # substitutions on the inupt.
        letter=Trade(letter)

        # If more than one rotor was used
        if hasattr(rotors, "__len__"):
            # "Pass through" each rotor.
            # First the first.
            letter = Swap(letter, rotors[0])
            # Then the rest after the reflections.
            for num in rotors[1:]:
                # Reflect the position every time
                # to make encryption revesible.
                letter = Swap(letter, int(len(ALPHABET)/2))
                letter = Swap(letter, num)
        else:
            # If only one rotor was used
            # then just do one swap.
            letter = Swap(letter, rotors)

        # Check for plugboard
        # substitutions on the outupt.
        letter=Trade(letter)

        # Add the character to the new string.
        new_message += letter

        # Advance the rotors
        rotors = Roll(rotors)

    # Print the new message.
    print(new_message)
##

# This runs the main function unless "QUIT" is entered.
while Run is True:
    Enigma()