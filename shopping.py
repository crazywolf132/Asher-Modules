#You can import any modules required here

#This is name of the module - it can be anything you want
moduleName = "shopping-list"
swapWords = "add | to | what's on | whats on | remove | from"
#These are the words you must say for this module to be executed
commandWords = "$x | $x | the shopping list"

shopping_list = []

#This is the main function which will be execute when the above command words are said
def execute(command):
    final_list = ''
    _string = ''
    tokens = str(command).split(' ')
    # Getting first and third words in the hopes the user says something like this...
    # Eg. 'Add watermelon to the shopping list'
    #      ^^^            ^^
    # And we get those words...
    _string = '{0} {1}'.format(tokens[0], tokens[2])

    if _string == 'add to':
        # We are adding to the shopping list now...
        # We are going to hope that the second word is the item.
        shopping_list.append(tokens[1])
        return 'Added.'
    elif _string == 'remove from':
        # We are now removing from the shopping list...
        # We are going to hope that the second word is the item.
        del shopping_list[int(shopping_list.index(str(tokens[1])))]
        return 'Removed.'
    elif _string == "what's on" or _string == 'whats on':
        # We are now going to read the items on the shopping list.
        for item in shopping_list:
            final_list += '{0}\n'.format(item)
            
        return final_list
