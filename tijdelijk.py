# 1.2
prijzen = {
"aardbei":3,
"vanille":4,
"chocolade":5
}
# 1.3
aanbieding=prijzen["vanille"] * .8
# 1.4 
reclame_tekst=f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts €  {aanbieding}"
print(reclame_tekst)
# 1.5 In tegenstellling tot de cursus wordt er keurig de waarde 3.2 afgedrukt hieronder een generieke oplossing voor het afdrukken tot de eerste 0
print(len(reclame_tekst))
positie=reclame_tekst.find('0')
if positie == -1:
    reclame_tekst2 = reclame_tekst
else:
    reclame_tekst2 = reclame_tekst[:positie]
print (reclame_tekst2)
# 1.6 
reclame_tekst3=reclame_tekst2.upper()
#print (reclame_tekst3)
# 1.7 
reclame_tekst4=reclame_tekst3.split(' ')
#print (reclame_tekst4)
# 1.8
'''
for el in reclame_tekst4:
  print(el)
'''
# 1.9
'''
for el in reclame_tekst4:
  print(el.lower())
'''
#1.10
for el in reclame_tekst4:
    if len(el)>4:
        print (el.lower())
    else:
        print (el.upper())
