"""
Programme qui compte le nombre de mots dans une chaîne de caractères
Nom: Liam Deehy-Rivest
Groupe: 123
"""
loop = True
while loop is True:
   def count_word(chaine):
       nouvelle_chaine = chaine.strip().split()
       return (len(nouvelle_chaine))

   chaine = input("Entrez la chaîne de caractère : ")
   print(count_word(chaine))

   reponse = input("Voulez-vous recommencer? Oui ou non").lower()
   if reponse == (f"non"):
       print("Merci et au revoir")
       loop = False
   else:
       pass

