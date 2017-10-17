#You can import any modules required here

#This is name of the module - it can be anything you want
moduleName = "shopping-list"
swapWords = "add | remove | delete | on | show | email | send"
#These are the words you must say for this module to be executed
commandWords = "$x | the shopping list"

shopping_list = []

#This is the main function which will be execute when the above command words are said
def execute(command):
    final_list = ''
    _string = ''
    command = command.lower().strip()
    tokens = str(command).split(' ')
    # Getting first and third words in the hopes the user says something like this...
    # Eg. 'Add watermelon to the shopping list'
    #      ^^^            ^^
    # And we get those words...
    _string = '{0} {1}'.format(tokens[0], tokens[2])

    for word in tokens:
        if word == 'add':
            shopping_list.append(str(tokens[int(tokens.index(str(word))) + 1]))
            return 'Added.'
        elif word == 'remove' or word == 'delete':
            del shopping_list[int(tokens.index(str(word))) + 2]
            return '{0}d.'.format(word[0].upper() + word[1:])
        elif word == 'on' or word == 'show':
            for item in shopping_list:
                if final_list == '':
                    final_list = '{0}'.format(item)
                else:
                    final_list += ', {0}'.format(item)

            return final_list
        elif word == 'email' or word == 'send':
            # Going to assume the next word after this is 'to'... so the name
            # will be 2 places after this word.
            print("")
