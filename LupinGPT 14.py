import time

# Fonction pour simuler un téléchargement
def telecharger():
    for i in range(1, 6):
        print("En cours de téléchargement... ", i*20, "%")
        time.sleep(1)
        print (" Vous êtes hacké")
        
        
# Boucle principale pour poser des questions et fournir des réponses
while True:
    # Demander une question ou salutation à l'utilisateur
    message = input("Bonjour madame, je me nome Lupin. Vous avez un rendez-vous avec Aymeric Simonet ? ")

    # Si l'utilisateur dit "au revoir", sortir de la boucle et fermer le programme
    if message == "au revoir":
        print("Au revoir, à bientôt !")
        break

    # Si l'utilisateur répond "oui" à la question, poser la question suivante
    elif message == "oui":
        print("Vous n'avez pas peur qu'il hack votre blog ou votre Gmail ?")

        # Attendre la réponse de l'utilisateur
        reponse = input()

        # Si l'utilisateur répond "oui", proposer une solution
        if reponse == "oui":
            print("J'ai une solution pour vous. Un antivirus nommé Shield Defender peut protéger votre ordinateur et vos données. Voulez-vous le télécharger ?")

            # Attendre la réponse de l'utilisateur
            reponse = input()

            # Si l'utilisateur répond "oui", simuler un téléchargement et afficher un message d'avertissement
            if reponse == "oui":
                print("En cours de téléchargement... :)")
                telecharger()

            # Si l'utilisateur répond "non", afficher un message de félicitations
            elif reponse == "non":
                print("Félicitations, vous êtes protégé contre les hackers !")

        # Si l'utilisateur répond "non", proposer une autre solution
        elif reponse == "non":
            print("Nous avons également une autre solution à vous proposer.")

    # Sinon, si l'utilisateur répond "non" à la question, poser la question suivante
    elif message == "non":
        print("Je suis désolé, je pense que vous avez fait une erreur. Pouvez-vous confirmer si vous avez bien un rendez-vous avec monsieur Simonet ?")

    # Sinon, si l'utilisateur dit quelque chose qui ne correspond pas aux cas ci-dessus, donner une réponse par défaut
    else:
        print("Je ne comprends pas, pouvez-vous reformuler votre question ou demande ?")