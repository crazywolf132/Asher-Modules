#You can import any modules required here

#This is name of the module - it can be anything you want
moduleName = "asher-math"
swapWords = "times | plus | add | minus | take | devide | devided | \\ | + | - | x | what is | what's"
#These are the words you must say for this module to be executed
commandWords = "$x | $x"

shopping_list = []

#This is the main function which will be execute when the above command words are said
def execute(command):
    answer = ''
    _string = ''
    command = command.lower().strip()
    tokens = str(command).split(' ')
    _string = '{0} {1}'.format(tokens[0], tokens[2])

    for word in tokens:
        if word == 'times' or word == 'x':
            y = int(tokens[int(tokens.index(str(word))) - 1])
            z = int(tokens[int(tokens.index(str(word))) + 1])
            answer = '{0} x {1} = {2}'.format(y, z, str(y * z))
        elif word == 'plus' or word == 'add' or word == '+':
            y = int(tokens[int(tokens.index(str(word))) - 1])
            z = int(tokens[int(tokens.index(str(word))) + 1])
            answer = '{0} + {1} = {2}'.format(y, z, str(y + z))
        elif word == 'devide' or word == 'devided' or word == '\\':
            y = int(tokens[int(tokens.index(str(word))) - 1])
            if word == 'devided':
                # We are going to assume the word after this is 'by'...
                z = int(tokens[int(tokens.index(str(word))) + 2])
            else:
                z = int(tokens[int(tokens.index(str(word))) + 1])
            answer = '{0} / {1} = {2}'.format(y, z, str(y / z))
        elif word == 'minus' or word == 'take' or word == '-':
            y = int(tokens[int(tokens.index(str(word))) - 1])
            z = int(tokens[int(tokens.index(str(word))) + 1])
            answer = '{0} - {1} = {2}'.format(y, z, str(y - z))

    return answer
