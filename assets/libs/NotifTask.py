def notif(title, message):
    import os
    from plyer import notification

    os.system("pip3 install plyer")

    # Paramètres de la notification
    #title = "Notification"
    #message = "Ceci est une notification du système d'exploitation"
    timeout = 10  # Durée d'affichage de la notification en secondes

    # Envoi de la notification
    notification.notify(title=title, message=message, timeout=timeout)