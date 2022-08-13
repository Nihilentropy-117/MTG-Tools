import math

import getDataMTG
import random
import pickle
def test():
    """
    filename = input("Filename of Cardlist? Default is \"cards.txt\"")
    if filename == "":
        filename = "cards.txt"
    cards = getDataMTG.get_cards(filename, "++")

    with open('temp.data', 'wb') as filehandle:
        # store the data as binary data stream
        pickle.dump(cards, filehandle)
    """
    with open('temp.data', 'rb') as filehandle:
        # read the data as binary data stream
        cards = pickle.load(filehandle)

    num_basics = 0
    num_nonbasics = 0
    for card in cards:
        if "Basic Land" in card["type"]:
            num_basics += 1
        elif "Land" in card["type"]:
            num_nonbasics += 1


    kept_hands = 0

    x = 0
    hands_to_try = 100000
    mulligan_to = [8]
    hands_tried = 0
    while hands_to_try > x:
        handsize = 8
        hand_basics = 0
        hand_tappedlands = 0
        hand_untappedlands = 0
        hand_aCMC = 0
        goodhand = False
        random.shuffle(cards)
        while handsize > 4 and goodhand is False:
            for card in cards[:handsize]:
                if "Basic Land" in card["type"]:
                    hand_basics += 1
                elif "Land" in card["type"] and " tapped" in card["oracle"]:
                    hand_tappedlands += 1
                elif "Land" in card["type"] and " tapped" not in card["oracle"]:
                    hand_untappedlands += 1

            hand_aCMC += int(card["cmc"])
            hand_fastland = hand_basics + hand_untappedlands
            hand_land = hand_basics + hand_untappedlands + hand_tappedlands
            if 1 < hand_land < 5 and hand_fastland > 0:
                kept_hands += 1
                goodhand = True
                mulligan_to.append(handsize - 1)
                hands_tried += 1
                break
            else:
                handsize -= 1
                random.shuffle(cards)
                hands_tried += 1
            if goodhand is True:
                break
        #print("{} land(s) in opening hand".format(hand_land))
        x += 1

    pc = kept_hands / hands_to_try
    print("Out of {} games hands simulated, {} were successful. This is {} total hands tested".format(hands_to_try, kept_hands,hands_tried))
    print("On average, we kept a hand size of {}, and succeeded in good land with 3 or less mulligans {}% of the time".format(math.floor(sum(mulligan_to) / len(mulligan_to)),pc))
