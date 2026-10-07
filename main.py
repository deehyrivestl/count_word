"""
Programme qui compte le nombre de mots dans une chaîne de caractère
Nom: Liam Deehy-Rivest
Groupe: 123
Vous devez avoir une fonction qui se nomme obligatoirement "count_word" et
elle doit recevoir un argument de type string.
La fonction devra retourner le nombre de mot contenu dans le paramètre.
Ensuite, votre programme doit afficher le résultat à l'écran.
"""
loop = True
while loop is True:
   def count_word(chaine):
       nouvelle_chaine = chaine.strip().split()
       return nouvelle_chaine

   chaine = input("Entrez la chaîne de caractère : ")
   count_word(chaine)
   chaine_développée = count_word(chaine)
   print(len(chaine_développée))
   reponse = input("Voulez-vous recommencer? Oui ou non").lower()
   if reponse == (f"non"):
       print("Merci et au revoir")
       loop = False
   else:
       pass

