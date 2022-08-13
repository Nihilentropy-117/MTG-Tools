import genCardShopList
import ManaBase
import deckTest
while True:
    try:
        runMode = int(input("1: Generate Card Shop Buylist \n2: Build Mana Base \n3: Test Deck \n\n Select Run Mode: "))
        break
    except ValueError:
        print("Invalid Entry")
        continue
while True:
    if runMode == 1:
        genCardShopList.gen_shop_list()
        break
    if runMode == 2:
        ManaBase.build_mana_base()
        break
    if runMode == 3:
        deckTest.test()
        break
    else:
        print("Invalid option, please try again\n")
        break
