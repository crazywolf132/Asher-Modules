#You can import any modules required here
import smtplib, email, imaplib
from email.Message import Message
from os.path import expanduser
#This is name of the module - it can be anything you want
moduleName = "shopping-list"
swapWords = "add | remove | delete | on | show | email | send"
#These are the words you must say for this module to be executed
commandWords = "$x | the shopping list"

shopping_list = []
users = {}
names = []
asherEmail = ''
asherPword = ''

#This is the main function which will be execute when the above command words are said
def execute(command):
    global asherEmail
    global asherPword
    with open("{0}/{1}/{2}".format(expanduser("~"), "Asher", "/asher.txt"), 'r') as _in:
        for line in _in:
            if asherEmail == '':
                asherEmail = line.strip()
            else:
                asherPword = line.strip()
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
            # 'Send the shopping list to mom'
            # 'Send dad the shopping list'
            # will be 2 places after this word.
            getUsers()
            for item in names:
                if tokens[int(tokens.index(str(word))) + 1] == str(item):
                    print('We found who to send it to: ' + str(item))
                    for prod in shopping_list:
                        if final_list == '':
                            final_list = '{0}'.format(prod)
                        else:
                            final_list += ', {0}'.format(prod)

                    sendOn(final_list, str(users[item]))
                    return 'Sent list to {0}'.format(item)
                elif tokens[-1] == str(item):
                    for prod in shopping_list:
                        if final_list == '':
                            final_list = '{0}'.format(prod)
                        else:
                            final_list += ', {0}'.format(prod)

                    sendOn(final_list, str(users[item]))
                    return 'Sent list to {0}'.format(item)

def getUsers():
    global users
    global names
    # This is going to be used to collect all the mirrors on the smart mirror.
    # We will then add them to a dictionary with their emails...
    # so then the user can refer to someone like this...
    # 'send shopping list to dad'
    holdLines = []
    userHolder = []
    with open("{0}/{1}/{2}".format(expanduser("~"), "Asher", "/users.js"), 'r') as _in:
        for line in _in:
            holdLines.append(str(line).strip())
    del holdLines[0]
    # In the user file, every 5 lines is a user... (the full user details.)
    _counter = 1
    #print(holdLines)
    _len = len(holdLines) - 1
    while _counter <= (_len / 5):
        _counter += 1
        userHolder.append('{0}$${1}$${2}$${3}$${4}'.format(str(holdLines[0]), str(holdLines[1]), str(holdLines[2]), str(holdLines[3]), str(holdLines[4])))
        del holdLines[0]
        del holdLines[0]
        del holdLines[0]
        del holdLines[0]
        del holdLines[0]

    for item in userHolder:
        # Get the name...
        _tokens = item.split(': {$$')
        _name = _tokens[0]
        # Get email.
        item = _tokens[1]
        _tokens = item.split("',$$")
        _token = _tokens[0].split("'")
        _email = _token[1]

        users[str(_name).lower()] = str(_email.lower())
        names.append(_name.lower())

def sendOn(_toSay, _email):
    try:
        from email.MIMEMultipart import MIMEMultipart
        from email.MIMEText import MIMEText
        msg = MIMEMultipart()
        msg['From'] = str(asherEmail)
        msg['To'] = str(_email)
        msg['Subject'] = str("Shopping list.")

        body = _toSay
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(str(asherEmail), str(asherPword))
        text = msg.as_string()
        server.sendmail(str(asherEmail), str(_email), text)
        server.quit()
    except:
        pass


execute('send list to me')
