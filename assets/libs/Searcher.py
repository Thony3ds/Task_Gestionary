import Run_App

def find_used(etat):
    if etat == "Category":
        return "Title"
    elif etat == "Title":
        return "Category"
    else:
        return "Title"

def update():
    if Run_App.settings.search_mod == "Title":
        Run_App.settings.search_mod = "Category"
    elif Run_App.settings.search_mod == "Category":
        Run_App.settings.search_mod = "Title"
    print(Run_App.settings.search_mod)

def search():
    print(Run_App.settings.search_mod)