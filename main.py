"""
Programme qui compte le nombre de mots dans une chaîne de caractères
Nom: Liam Deehy-Rivest
Groupe: 123
"""
loop = True

def count_word(texte):
    nouvelle_chaine = texte.strip().split()
    return len(nouvelle_chaine)

while loop is True:
    chaine = input("Entrez la chaîne de caractère : ")
    print(count_word(chaine))

    reponse = input("Voulez-vous recommencer? Oui ou non").lower()
    if reponse == f"non":
       print("Merci et au revoir")
       loop = False
    else:
       pass

