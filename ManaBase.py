import math
import getDataMTG


def build_mana_base():
    # Define Globals
    total_mana = dict(White=0, Blue=0, Black=0, Red=0, Green=0, Colorless=0, Generic=0)
    required_lands = dict(White=0, Blue=0, Black=0, Red=0, Green=0, Colorless=0)

    # Get file name from user containing card list
    filename = input("Filename of Cardlist? Default is \"cards.txt\"")
    if filename == "":
        filename = "cards.txt"
    cards = getDataMTG.get_cards(filename, "++")
    j = 0
    # Ask user information about their deck.
    while True:
        try:
            mana_rocks = int(input("How many of your cards are mana rocks?"))
            ramp_spells = int(input("How many of your cards are ramp spells?"))
            break
        except ValueError:
            print("Invalid Entry")
            continue

    while True:
        priority_color = input("What is your early game priority color? (White Blue Black Red Green Colorless Generic)")
        if priority_color in {"White", "Blue", "Black", "Red", "Green", "Colorless", "Generic"}:
            break
        else:
            print("Invalid Response")
            continue

    # Find and assign all mana symbols of all cards
    for item in cards:
        for mana in item["cost"]:
            if mana == "W":
                total_mana["White"] += 1
            elif mana == "U":
                total_mana["Blue"] += 1
            elif mana == "B":
                total_mana["Black"] += 1
            elif mana == "R":
                total_mana["Red"] += 1
            elif mana == "G":
                total_mana["Green"] += 1
            elif mana == "C":
                total_mana["Colorless"] += 1
            elif mana == "{" or "}":
                pass
            else:
                print("Mana error")
    totalsymbols = sum(total_mana.values())

    # Determine average CMC of all cards
    total_cmc = 0
    for card in cards:
        total_cmc += int(card["cmc"])
    average_cmc = round(total_cmc / len(cards), 2)

    # Determine how many lands deck should contain
    totalLands = 40 - (math.floor(ramp_spells) / 3) - (math.floor(mana_rocks) / 3)

    # Determine how many of each land deck should contain
    for color in total_mana:
        if total_mana[color] != 0:
            anyMana = required_lands[color] = math.floor((total_mana[color] / totalsymbols) * totalLands)

    # Print results to user
    print("In your deck, {} is the average cmc.".format(average_cmc))
    print("You have a estimated total of {} lands required".format(totalLands))
    for x, y in required_lands.items():
        if y > 0:
            print("You need {} lands generating {} Mana".format(y, x))
    anyMana == 0 if anyMana <= 0 else print(
        "You should also have an additional {} lands producing either {} Mana or Generic Mana.".format(anyMana,
                                                                                                       priority_color))
