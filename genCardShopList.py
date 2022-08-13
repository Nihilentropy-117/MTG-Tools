import getDataMTG


def gen_shop_list():
    filename = input("Filename of Cardlist? Default is \"cards.txt\"")
    if filename == "":
        filename = "cards.txt"
    tags = getDataMTG.get_cards(filename, "fuzzy")

    all_sets = set()
    for item in tags:
        all_sets.add(item["set_name"])

    sets_with_under2 = []
    sets_with_over2 = []
    sets_with_no_price = []

    for x in tags:
        if not x["price"]:
            x["price"] = 0
        else:
            if 0 < float(x["price"]) <= 2:
                sets_with_under2.append(x["set_name"])
            elif float(x["price"]) > 2:
                sets_with_over2.append(x["set_name"])
            else:
                sets_with_no_price.append(x["set_name"])

    file = open("output.txt", 'w')

    file.write("\t\t\tCards under $2.00\n")

    for sets in sets_with_under2:

        file.write(sets + "\n")
        for card in tags:
            if 0 < float(card["price"]) <= 2 and card["set_name"] == sets:
                file.write("\t" + card["name"] + "@" + card["price"] + "\n")

        file.write("\n")

    file.write("\t\t\tCards over $2.00\n")
    for sets in sets_with_over2:

        file.write(sets + "\n")
        for card in tags:
            if float(card["price"]) > 2 and card["set_name"] == sets:
                file.write("\t" + card["name"] + "@" + card["price"] + "\n")

        file.write("\n")

    file.write("\t\t\tCards With No Price\n")

    for sets in sets_with_no_price:

        file.write(sets + "\n")
        for card in tags:
            if float(card["price"]) == 0 and card["set_name"] == sets:
                file.write("\t" + card["name"] + " has no price data available" + "\n")

        file.write("\n")

    file.close()
    print("Written to file: \"output.txt\"")
