from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs ,korting):
    reclameprijs=("%1.2f " % (prijs*(1-korting)))  
    return(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak} , van {prijs} euro voor {reclameprijs}euro.")

print(aanbieding_1("aardbei", 4 ,0.1))

def inkomsten_totaal(inkomsten,btw):
    totaal_inkomsten=sum(inkomsten)
    btw_bedrag=("%1.2f " %(btw*(totaal_inkomsten/1+btw)))
    return (f"Het totaal van alle inkomsten van deze week is {totaal_inkomsten} euro, waarover {btw_bedrag} euro btw betaald dient te worden.")
 
inkomsten=[220, 430, 125, 160, 205, 90, 345]   
print (inkomsten_totaal(inkomsten,0.09))

def laag_en_hoog(mijn_lijst):
    hoog=max(mijn_lijst)
    laag=min(mijn_lijst)
    hoog_laag=[hoog,laag]
    return hoog_laag

mijn_lijst=inkomsten
print (laag_en_hoog(mijn_lijst))

def gemiddelde(mijn_lijst):
    gem=("%1.2f " % (sum(mijn_lijst)/len(mijn_lijst)))
    return  (f"De gemiddelde inkomsten deze week zijn {gem}euro.")
   
mijn_lijst=inkomsten
print (gemiddelde(mijn_lijst))

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

invoer_lijst=[10,5,3,2,1,2,9]
print (meervoudig(invoer_lijst))

def combinatie(invoer_lijst_2):
    korte_lijst=meervoudig(invoer_lijst_2)
    return mijn_functie_2(korte_lijst[0],korte_lijst[1])

#invoer_lijst_2=invoer_lijst
#print (combinatie(invoer_lijst_2))