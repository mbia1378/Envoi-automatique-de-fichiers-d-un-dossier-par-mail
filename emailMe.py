#!/usr/bin/python3

'''
Obtenir la liste du contenu d'un répertoire dans un e-mail.
Utile pour vérifier si une sauvegarde s'est terminée avec succès.
Par exemple : si vous voyez de nouveaux fichiers dans l'e-mail, vous savez que
la sauvegarde est terminée. Fichiers classés par ordre alphabétique inverse
pour accepter les noms de fichiers qui représentent un horodatage.
* Utilise Gmail pour envoyer le message électronique. Vous aurez besoin d'identifiants Gmail valides.
'''

import smtplib, os, sys

gmailUsername = ("Email")
gmailPassword = ("Mot_De_Passe")
senderName = ("OS Linux")
receiverName =("Cyrille")
sender = ("Email")

receivers = ['mail1','mail2'] #Liste des adresses e-mail, séparées par des virgules.
mimeVersion = ("1.0")
contentType = ("text/plain")
subject = ("Sauvegardes du dossier de fichiers")

path = ("/chemin/vers/dossier/")
dirs = os.listdir(path)

fileList = []
recipients = ''.join(receivers)

for file in dirs:
    fileList.append("{}\n".format(file))

fileList.reverse()
body = "".join(fileList)

message = "De: "+senderName+" <"+sender+">\nPour: "+receiverName+" <"+recipients+">\nMime version: "+mimeVersion+"\nContent-type: "+contentType+"\nSujet: "+subject+"\n\n{}".format(body)

try: 
    smtpObj = smtplib.SMTP(host='smtp.gmail.com', port=587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.ehlo()
    smtpObj.login(gmailUsername,gmailPassword)
    smtpObj.sendmail(sender, receivers, message)
    smtpObj.quit()
    print ("Mail envoyé")
except smtplib.SMTPException as e:
    error_code = e.smtp_code
    error_message = e.smtp_error
    print(error_code)
    print(error_message)
    print ("Erreur : Email non envoyé")