import time
import scrython
import sys

deck = []


def get_cards(filename, mode):
    if mode == "list":
        mod = "++"
    elif mode == "deck":
        mod = ""

    file = open(filename, 'r')
    imported_cards = file.readlines()
    file.close()

    for line in imported_cards:
        time.sleep(.05)

        try:
            data = scrython.cards.Search(q='{}!"{}"'.format(mod, line))
        except scrython.ScryfallError as e:
            error = "Input file error. Check " + line
            # print(str(e.error_details['status']) + ' ' + e.error_details['code'] + ': ' + e.error_details['details'])
            sys.exit(error)
        total_price = 0
        for inputcard in data.data():
            # x = inputcard['name'].upper() + "_" + inputcard['set'].upper()
            deck.append(dict(name=inputcard['name'].upper(),
                             set=inputcard['set'].upper(),
                             set_name=inputcard['set_name'].upper(),
                             price=inputcard['prices']["usd"],
                             color=inputcard['colors'],
                             cost=inputcard['mana_cost'],
                             type=inputcard['type_line'],
                             oracle=inputcard['oracle_text'],
                             cmc=inputcard['cmc'])
                        )
            print("Gathering data for \"{}\" from api.scryfall.com".format(inputcard["name"]))

    print("\n\n\n")
    return deck
