import Run_App

def find_used(etat):
    if etat == "Category":
        return "Title"
    elif etat == "Title":
        return "Category"
    else:
        return "Title"

def search(mod):
    print(mod)