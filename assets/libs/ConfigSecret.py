from assets.libs import CryptApp
import os, json

def valeur_existe(donnees_json, valeur_recherche):
    for valeur in donnees_json.values():
        if valeur == valeur_recherche:
            return True
        elif isinstance(valeur, dict):
            if valeur_existe(valeur, valeur_recherche):
                return True
        elif isinstance(valeur, list):
            for element in valeur:
                if isinstance(element, dict) and valeur_existe(element, valeur_recherche):
                    return True
    return False

def crypt(file, key):
    tfile = json.load(file)
    if tfile["secret"] == 1 and key != "":
        content = CryptApp.crypt_decrypt(entry_file=file, exit_file=file, key=key)
        to_put = '{ "crypted": "'
        to_put = to_put + f'{content}", "secret": 1 '
        to_put = to_put + "}"
        to_put2 = json.dumps(to_put)
        with open(file, "w") as f:
            f.write(to_put2)
            f.close()
        return True
    else:
        return False
def decrypt(file, key):
    tfile = json.load(file)
    if tfile["secret"] == 1 and valeur_existe(tfile, "crypted"):
        content = CryptApp.crypt_decrypt(entry_file=file, exit_file=file, key=key)
        return True
    elif key == "" and valeur_existe(tfile, "crypted") == False:
        return True
    else:
        return False
