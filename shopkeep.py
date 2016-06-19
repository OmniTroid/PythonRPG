__author__ = 'DS'

print "L O L"

global playercash
playercash = 200
value = {"apple": 10, "rope": 20, "bedroll": 100, "bomb": 30}
playerinventory = {"apple": 3, "rope": 7, "bedroll": 1, "bomb": 0}
shopkeepinventory = {"apple": 0, "rope": 30, "bedroll": 3, "bomb": 20}

singular = {"bomb": "Bomb", "apple": "Apple", "bedroll": "Bedroll", "rope": "Rope"}
plural = {"bomb": "Bombs", "apple": "Apples", "bedroll": "Bedrolls", "rope": "Ropes"}


def inventory():
    global playercash
    for item in playerinventory:
        if playerinventory[item] == 1:
            print singular[item] + ":", playerinventory[item]
        else:
            print plural[item] + ":", playerinventory[item]
    print "Gold:", playercash


def town():
    while True:
        choice = raw_input("> ")
        if "shopkeep" in choice:
            print "'Welcome, stranger'"
            shopkeep()
        elif "apple" in choice:
            appleseller()
        elif "castle" in choice:
            castle()
        elif "inventory" in choice:
            inventory()
        elif "leave" in choice:
            print "You leave the town. Goodbye!"
            exit(0)
        else:
            print "You wander around aimlessly for a bit."


def shopkeep():
    while True:
        choice = raw_input("> ")
        if choice == "help":
            print "list: lists the items for sale"
            print "sell <quantity> <item>: sells the given item in given quantity from your inventory"
            print "buy <quantity> <item>: buys the given item in given quantity from the shop"

        elif "list" in choice:
            for item in shopkeepinventory:
                if shopkeepinventory[item] == 1:
                    singleorplural = singular[item].lower()
                else:
                    singleorplural = plural[item].lower()
                if shopkeepinventory[item] == 0:
                    pass
                else:
                    print shopkeepinventory[item], singleorplural + ", price:", int(round(value[item]*1.3)), "gold"

        elif "inventory" in choice:
            inventory()

        elif "sell" in choice:
            splitchoice = choice.split(' ')
            if len(splitchoice) == 3:
                sell(splitchoice[1], splitchoice[2])
            elif len(splitchoice) < 3:
                print "Error: not enough arguments"
            else:
                print "Error: too many arguments"

        elif "buy" in choice:
            splitchoice = choice.split(' ')
            if len(splitchoice) == 3:
                buy(splitchoice[1], splitchoice[2])
            elif len(splitchoice) < 3:
                print "Error: not enough arguments"
            else:
                print "Error: too many arguments"

        elif "bye" in choice or "leave" in choice:
            print "'Safe travels!'"
            town()

        else:
            print "'Ehh can't say I know what you're tryin' to say, stranger.'"


def sell(amount, item):
    try:
        intamount = int(amount)
        enoughitems = (playerinventory[item] >= intamount)
    except KeyError:
        print "Error: item does not exist"
    except ValueError:
        print "Error: the second argument must be a number"

    else:
        if enoughitems:
            total = int(round(value[item]*0.7))*intamount

            if intamount == 1:
                singleorplural = singular[item].lower()

            else:
                singleorplural = plural[item].lower()

            print "%d %s eh? I can give you %d gold for that. Deal?" % (intamount, singleorplural, total)
            answer = raw_input("> ")

            if "yes" in answer.lower() or "deal" in answer.lower():
                print "'Alright, it's a deal.'"
                global playercash
                playercash += total
                playerinventory[item] -= intamount
                shopkeepinventory[item] += intamount
                print "Lost %d %s. Got %d gold." % (intamount, singleorplural, total)
                print "'Anything else ya need?'"

            else:
                print "'Alright, then. No deal it is.'"

        else:
            print "Error: you do not have enough of the selected item"


def buy(amount, item):
    global playercash
    try:
        intamount = int(amount)
        enoughitems = (shopkeepinventory[item] >= intamount)
        total = int(round(value[item]*1.3))*intamount
        enoughmoney = playercash >= total
    except KeyError:
        print "Error: item does not exist"
    except ValueError:
        print "Error: the second argument must be a number"

    else:
        if enoughitems and enoughmoney:

            if intamount == 1:
                singleorplural = singular[item].lower()

            else:
                singleorplural = plural[item].lower()

            print "'%d %s eh? I'll need %d gold for that. Deal?'" % (intamount, singleorplural, total)
            answer = raw_input("> ")

            if "yes" in answer.lower() or "deal" in answer.lower():
                print "'Alright, it's a deal.'"
                playercash -= total
                playerinventory[item] += intamount
                shopkeepinventory[item] -= intamount
                print "Lost %d gold. Got %d %s." % (total, intamount, singleorplural)
                print "'Anything else ya need?'"

            else:
                print "'Alright, then. No deal it is.'"
        elif not enoughmoney:
            print "Error: you do not have enough money."
        else:
            print "Error: the shop does not have enough of the selected item"


def appleseller():
    print "The apple seller seems to be out."
    town()


def castle():
    print "There is nothing interesting here. For now."
    town()

print "It's a quiet day in town, do you go to the shopkeep, the apple seller, the castle or open your inventory?"
town()





