"""This Module contains basic functions that I use in various programs"""

# Variable Definitions

__version__ = "Alpha"
__author__ = "Rodrigo 'ItsPaper' Muñoz"
__email__ = "rodrigo.mcuadrada@gmail.com"
__license__ = "MIT"
__date__ = "9th of August 2017"

# functions


def cls():
    """This function clears the shell screen"""
    print("\n" * 50)


def pause():
    """This function pauses the program until the user presses enter key"""
    x = input("PRESS ENTER TO CONTINUE...")


def confirm():
    """This Function asks user for confirmation"""
    confirmation = input("Do you wish to confirm? Y-N")
    confirmation = confirmation.lower()
    if confirmation == "y":
        return True
    else:
        print("Confirmation Failed!")
        return False
