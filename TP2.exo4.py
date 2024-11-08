personne = int(input("Entrez le nombre de personne(s) conviées à la fondue : "))
print("Pour faire un fondue fribourgeoise pour ", personne, " personnes, il vous faut :")
fromage = personne * 200
eau = 0.5 * personne
ail = eau
pain = 100 * personne
print ("- ",fromage, "gr de fromage")
print ("- ",eau, "dl d'eau")
print ("- ",ail, "gousse(s) d'ail")
print ("- ",pain, "gr de pain")