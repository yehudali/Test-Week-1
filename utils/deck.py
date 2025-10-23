def create_card(rank:str,suite:str) -> dict:
    rank=rank
    suite=suite
    #Determining the value of the card by rank
    value_card=0
    if rank=="2":
        value_card=2
    elif rank =="3":
        value_card=3
    elif rank =="4":
        value_card=4
    elif rank =="5":
        value_card=5
    elif rank =="6":
        value_card=6
    elif rank =="7":
        value_card=7
    elif rank =="8":
        value_card=8
    elif rank =="9":
        value_card=9
    elif rank =="10":
        value_card=10

    elif rank =="j":
        value_card=11
    elif rank =="q":
        value_card=12
    elif rank =="k":
        value_card=13
    elif rank =="a":
        value_card=14
    #creat card:
    card = {"rank": rank, "suite": suite, "value": value_card}

    return card
# #test
# print(create_card("a","H"))




def compare_cards(p1_card:dict, p2_card:dict) -> str:
    try:
        p1=p1_card["value"]
        p2=p2_card["value"]
        if p1 > p2:
            return "p1"
        elif p1 == p2:
            return 'WAR'
        else:
            return "p2"
    except:
        raise TypeError("I was unable to access the card value to compare the cards.")




def create_deck() -> list[dict]:
    #מאגר סוגי דרגות, וסוגים, של הקלפים
    rank=["2","3","4","5","6","7","8","9","10","j","q","k","a"]
    suite=["H","C","D","S"]
    deck=[]
    for i in rank:
        for j in suite:
            deck.append(create_card(i,j))
    return deck


import random
def shuffle(deck:list[dict]) -> list[dict]:
    deck_mixed=deck[::]
    for i in range(900):
        random_num1=random.randrange(0, 52)
        random_num2=random.randrange(0, 52)
        if random_num1 != random_num2:
            # random_card1=deck_mixed[random_num1]
            # random_card2=deck_mixed[random_num2]
            deck_mixed[random_num1],deck_mixed[random_num2]=deck_mixed[random_num2],deck_mixed[random_num1]
    #The deck after mixing
    return deck_mixed




#שימוש לדוגמא
if __name__ == "__main__":
    print("start")
    #יצירת מילון
    print(create_deck())
    #יצירה וערבוב מילון
    print(shuffle(create_deck()))
