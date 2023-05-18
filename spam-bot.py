import time

# Liste des messages à envoyer
messages = [
    "Bonjour !Félicitations ! ",
    " Nous sommes ravis de vous informer que vous avez remporté le prix du meilleur avis sur Tripadvisor. Votre contribution précieuse et votre expérience partagée ont été reconnues par la communauté de voyageurs du monde entier..",
    "Votre avis élogieux et détaillé a aidé de nombreux voyageurs à prendre des décisions éclairées et à vivre des expériences mémorables. Votre engagement à partager vos expériences positives est vraiment apprécié, et nous sommes fiers de vous compter parmi nos membres les plus influents..",
    " En reconnaissance de votre contribution exceptionnelle, nous vous offrons un voyage gratuit 3 semaines  . Veuillez nous contacter dès que possible pour obtenir plus de détails adresse suivant de  https wwww.Tripadvisor-winner.com",
    "Encore une fois, toutes nos félicitations pour cette réussite. Continuez à partager vos aventures et à inspirer les autres avec vos récits de voyage.."
]

# Fonction pour envoyer un message
def envoyer_spammessage(message):
    print("Envoi du message-spam : ", message)
    # Code pour envoyer réellement le message (par exemple, une API d'envoi de message)
    time.sleep(1)  # Pause d'une seconde pour simuler l'envoi
    print("Message envoyé avec succès.")

# Boucle pour envoyer les messages
for message in messages:
    envoyer_spammessage(message)
    print()  # Ajouter une ligne vide pour séparer les messages

print("Tous les spam-messages ont été envoyés.")
