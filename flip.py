#You can import any modules required here
from random import *

#This is name of the module - it can be anything you want
moduleName = "flip-coin"
swapWords = ""
#These are the words you must say for this module to be executed
commandWords = "flip a coin"

#This is the main function which will be execute when the above command words are said
def execute(command):
    x = randint(1, 2)
    if str(x) == '1':
        return 'Heads'
    else:
        return 'Tails'
