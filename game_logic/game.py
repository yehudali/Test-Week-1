def create_player(name="ai") -> dict:
    user_name=name
    hand=[]
    won_pile=[]
    player={"user_name":user_name,"hand":hand,"won_pile":won_pile}
    #return player_dict:
    return player


from utils.deck import *
def init_game()->dict:
    random_neme="yehuda"
    p1=create_player(random_neme)
    p2=create_player()
    #Creating and mixing a package
    deck_mixed=shuffle(create_deck())
    #Dealing cards
    p1["hand"]=deck_mixed[:26]
    p2["hand"]=deck_mixed[26:]

    x={"deck":"deck_mixed", "player_1": p1,"player_2": p2}

    return x



from utils.deck import shuffle
def play_round(p1:dict,p2:dict):
    w=p1["hand"][0].get
    x=p2["hand"][0].get
    test=shuffle(w,x)


    return