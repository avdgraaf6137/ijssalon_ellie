def presenteer(d={},totaal=0):
    #mijn_dict = {'vis' : 10, 'vlees': 25, 'overig' : 15}
    #totaal=50
    mijn_dict=d
    for x in mijn_dict:
        print(x,":",mijn_dict[x]," euro.")
    print(27*"=")
    print(f"totaal : {totaal} euro.")
