#You can import any modules required here
from random import *

#This is name of the module - it can be anything you want
moduleName = "asher-math"
swapWords = "a | the | dice | die"
#These are the words you must say for this module to be executed
commandWords = "roll | $x | $x"

shopping_list = []

#This is the main function which will be execute when the above command words are said
def execute(command):
    return randint(1, 6)
