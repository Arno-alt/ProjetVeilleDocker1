rep = 0
rep = input("1 : Ajouter \n 2 : Afficher la liste \n")

rep = int(rep)
if rep == 1:
    nom = input("donner votre nom \n")
    prenoms = input("donner vos prenom \n")
    mail = input("donner votre mail \n")
    numero = input("donner votre numero \n")
    import datetime
    date_saisir = datetime.datetime.now()
    jour =(date_saisir.strftime("%d"))
    mois = (date_saisir.strftime("%m"))
    annee = (date_saisir.strftime("%Y"))
    date_saisir = jour+" "+mois+" "+annee

    tab = [date_saisir," ", nom," ", prenoms," ", mail," ", numero]
    filout = open("zoo.txt", "a")
    for x in tab :
        filout.write(x)

    filout.close()

elif rep == 2 :
    filout = open("zoo.txt", "r")
    print(filout.read())



