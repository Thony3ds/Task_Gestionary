import json


def update_app():
    import tempfile, os

    # Créer un fichier temporaire
    temp_dir = tempfile.mkdtemp(prefix="Task_Gestionary")  # Crée un répertoire temporaire
    temp_file = os.path.join(temp_dir, "updater.txt")  # Chemin du fichier temporaire
    temp_file2 = os.path.join(temp_dir, "path.json")  # Chemin du fichier temporaire

    #Importer le code
    f = open("assets/config/updater.txt", "r")
    # Écrire le code du script temporaire
    script_code = f.read()
    f.close()

    # Écrire le code dans le fichier temporaire
    with open(temp_file, "w") as file:
        file.write(script_code)

    with open(temp_file2, "w") as file:
        var = {
            "path_dir": temp_dir, "path_pytemp": temp_file, "path_txtfile": temp_file2
        }
        file.write(json.dumps(var))
    repertoire_courant = os.path.dirname(os.path.abspath(__file__))
    os.system(f"python3 {temp_file}")

def temp_delete():
    import os, tempfile
    # Nom du répertoire temporaire
    nom_repertoire_temporaire = "Task_Gestionary"

    # Rechercher le fichier temporaire en parcourant le répertoire temporaire
    for root, dirs, files in os.walk(tempfile.gettempdir()):
        if nom_repertoire_temporaire in dirs:
            chemin_repertoire_temporaire = os.path.join(root, nom_repertoire_temporaire)
            chemin_fichier_temporaire = os.path.join(chemin_repertoire_temporaire, "updater.txt")
            if os.path.exists(chemin_fichier_temporaire):
                # Utilisez chemin_fichier_temporaire pour accéder au fichier temporaire
                temp_dir = chemin_repertoire_temporaire
                temp_file = chemin_fichier_temporaire
                break
    # Nettoyer le fichier temporaire et le répertoire temporaire
    os.remove(temp_file)
    os.remove(f"{temp_dir}path.json")
    os.rmdir(temp_dir)