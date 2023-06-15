import tkinter as tk
from tkinter import ttk
import os, datetime, json, glob
from assets.libs import EditTask, Settings

app = tk.Tk()
app.option_add('*Font', "Ubuntu")
app.option_add('*Label.foreground', 'white')
app.option_add('*Label.background', 'black')
date_actuelle = datetime.date.today()

class settings():
    f = open("assets/config/settings.json", "r")
    set_data = json.load(f)
    f.close()
    task_max = set_data["task_max"]

def count_files():
    file_pattern = os.path.join("assets/tasks/", "*")
    files = glob.glob(file_pattern)
    file_count = len(files)
    file_count = file_count - 1
    return file_count

def delete_task():
    os.remove(task_config_path)
    new_window.destroy()
    trie_start()

def edit_task():
    new_window.destroy()
    edit_task_window = EditTask.run(task_config_path)
    edit_task_window.wait_window()  # Attendre la fermeture de la fenêtre EditTask

    trie_start()
def config_task(event):
    global task_config_path, new_window
    # Récupérer l'élément sélectionné dans la Listbox
    index = listbox.curselection()
    element_selectionne = listbox.get(index)

    # Parcourir les fichiers JSON dans le répertoire
    for filename in os.listdir("assets/tasks/"):
        if filename.endswith(".json"):
            filepath = os.path.join("assets/tasks/", filename)
            # Charger les données à partir du fichier JSON en tant que dictionnaire
            with open(filepath, "r") as json_file:
                json_data = json.load(json_file)

            # Vérifier si l'élément sélectionné est présent dans les données
            if json_data["title"] == element_selectionne:
                task_config_path = filepath
                break

    # Créer une nouvelle fenêtre
    new_window = tk.Toplevel(app)
    new_window.config(bg="black")
    new_window.title(element_selectionne)
    file = open(task_config_path, "r")
    into_file = json.load(file)
    lab1 = tk.Label(new_window, text=f'Title: {into_file["title"]}')
    lab1.pack()
    lab2 = tk.Label(new_window, text=f'Description: {into_file["description"]}')
    lab2.pack(pady=10)
    lab3 = tk.Label(new_window, text=f'Limit date: {into_file["limit_date"]}')
    lab3.pack(pady=10)
    lab4 = tk.Label(new_window, text=f'Category: {into_file["category"]}')
    lab4.pack(pady=10)
    lab5 = tk.Label(new_window, text=f'State: {into_file["State"]}')
    lab5.pack(pady=10)
    bu1 = tk.Button(new_window, text="Edit task", command=edit_task)
    bu1.pack(pady=10)
    bu2 = tk.Button(new_window, text="Delete task", fg="red", command=delete_task)
    bu2.pack(pady=10)

def trie_start():
    task_num = count_files()
    var = True
    running = True
    num = 0
    listbox.delete(0, tk.END) # Delete all element in listbox
    print("trie start while")
    while running:
        num = num + 1
        file_name = f"assets/tasks/task{num}.json"
        var = os.path.exists(file_name)
        if var:
            with open(file_name, "r") as tfile:
                reading = json.load(tfile)
                listbox.insert(tk.END, reading["title"])
            task_num = task_num - 1
        if var is not True and task_num == 0:
            running = False
        if num >= settings.task_max:
            break

def update_class_task(option):
    if option == "Trier par Date":
        listbox.delete(0, tk.END)  # Efface tous les anciens éléments de la Listbox

        items = []
        num = 0
        while True:
            num += 1
            file_name = f"assets/tasks/task{num}.json"
            if not os.path.exists(file_name):
                break

            with open(file_name, "r") as tfile:
                reading = json.load(tfile)
                title = f'{reading["title"]} for: {reading["limit_date"]}'
                limit_date = datetime.datetime.strptime(reading["limit_date"], "%d/%m/%Y")
                items.append((title, limit_date))

        items.sort(key=lambda x: x[1])  # Trie les éléments par date

        for item in items:
            listbox.insert(tk.END, item[0])  # Ajoute les éléments triés dans la Listbox
    elif option == "Trier par Default":
        trie_start()

def create_optbar():
    # Options de la liste déroulante
    options = ["Trier par Date", "Trier par Default", "Afficher les secrets"]

    # Fonction appelée lorsque l'option est sélectionnée
    def on_select(event):
        selected_option = dropdown.get()
        update_class_task(selected_option)

    # Création de la liste déroulante
    dropdown = ttk.Combobox(app, values=options, width=15)
    dropdown.pack(anchor=tk.NW)

    # Définition de la fonction à appeler lorsque l'option est sélectionnée
    dropdown.bind("<<ComboboxSelected>>", on_select)

def serialize_date(date):
    if isinstance(date, datetime.date):
        next_day = date + datetime.timedelta(days=1)
        return next_day.strftime('%d/%m/%Y')
    raise TypeError(f'Object of type {date.__class__.__name__} is not JSON serializable')

def test_gen_list():
    for i in range(100):
        listbox.insert(tk.END, f'Élément {i + 1}')

def get_date():
    day = date_actuelle.day
    month = date_actuelle.month
    year = date_actuelle.year
    return f"{day}/{month}/{year}"

def createTask2():
    if os.path.exists("assets/tasks/") == False:
        os.mkdir("assets/tasks/")
    new = {}
    new["title"] = inp_title.get()
    new["description"] = inp_desc.get()
    new["State"] = "In process"
    day_value = day_var.get()
    month_value = month_var.get()
    year_value = year_var.get()
    if day_value and month_value and year_value:
        inp_date = "{}/{}/{}".format(day_value, month_value, year_value)
        new["limit_date"] = inp_date
    else:
        new["limit_date"] = date_actuelle + datetime.timedelta(days=1)  # Ou une valeur par défaut si aucune date n'est entrée
    new["category"] = inp_category.get()
    json_write = json.dumps(new, default=serialize_date)
    num = 0
    var = True
    while var:
        num = num + 1
        if os.path.exists(f"assets/tasks/task{str(num)}.json") == True:
            pass
        else:
            var = False
    newf = open(f"assets/tasks/task{num}.json", "w+")
    newf.write(json_write)
    newf.close()
    # Mettre à jour la Listbox
    trie_start()
    newt.destroy()

def createDateEntry():
    global day_var, month_var, year_var
    # Création des variables pour stocker les valeurs du champ d'entrée
    day_var = tk.StringVar()
    month_var = tk.StringVar()
    year_var = tk.StringVar()

    # Frame pour la saisie de la date
    date_frame = ttk.Frame(newt)
    date_frame.pack(padx=10, pady=10)

    # Label et champ d'entrée pour le jour
    day_label = ttk.Label(date_frame, text="Jour:")
    day_label.grid(row=0, column=0, padx=5, pady=5)
    day_entry = ttk.Spinbox(date_frame, from_=1, to=31, width=5, textvariable=day_var)
    day_entry.grid(row=0, column=1, padx=5, pady=5)

    # Label et champ d'entrée pour le mois
    month_label = ttk.Label(date_frame, text="Mois:")
    month_label.grid(row=0, column=2, padx=5, pady=5)
    month_entry = ttk.Spinbox(date_frame, from_=1, to=12, width=5, textvariable=month_var)
    month_entry.grid(row=0, column=3, padx=5, pady=5)

    # Label et champ d'entrée pour l'année
    year_label = ttk.Label(date_frame, text="Année:")
    year_label.grid(row=0, column=4, padx=5, pady=5)
    year_entry = ttk.Entry(date_frame, width=10, textvariable=year_var)
    year_entry.grid(row=0, column=5, padx=5, pady=5)

    # obtenir la date
    datelab = tk.Label(newt, text=get_date())
    datelab.pack(pady=10)

def createTask():
    global newt, inp_title, inp_desc, inp_category
    newt = tk.Tk()
    newt.title("New Task")
    newt.geometry("500x500")
    newt.config(bg="black")
    newt.option_add('*Font', "Ubuntu")
    newt.option_add('*Label.foreground', 'white')
    newt.option_add('*Label.background', 'black')
    lab1 = tk.Label(newt, text="Title:")
    lab1.pack()
    inp_title = tk.Entry(newt)
    inp_title.pack(pady=10)
    lab2 = tk.Label(newt, text="Description:")
    lab2.pack(pady=10)
    inp_desc = tk.Entry(newt)
    inp_desc.pack(pady=10)
    inp_desc.config(width=40)
    lab3 = tk.Label(newt, text="Date Limite:")
    lab3.pack(pady=10)
    createDateEntry()
    lab4 = tk.Label(newt, text="Category:")
    lab4.pack(pady=10)
    inp_category = tk.Entry(newt)
    inp_category.pack(pady=10)
    bu = tk.Button(newt, text="Create", command=createTask2)
    bu.pack(pady=10)

def resize_listbox(event):
    # Obtenir la nouvelle largeur et hauteur de la fenêtre
    width = event.width
    height = event.height

    # Redimensionner la Listbox en fonction de la nouvelle taille de la fenêtre
    listbox.config(width=width // 1200, height=height // 1000)

def appli():
    app.title("Gestionnaire de Taches")
    app.geometry("750x550")
    app.config(bg="black")
    app.minsize(width=350, height=350)

    lab1 = tk.Label(app, text="Task Gestionary")
    lab1.place(x=0, y=0)
    lab_credits = tk.Label(app, text="app create by Thony3ds")
    lab_credits.pack(anchor=tk.NE)

    # Créer une scrollbar
    global scrollbar, listbox, new_bu
    scrollbar = tk.Scrollbar(app)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    # Créer une liste
    listbox = tk.Listbox(app, yscrollcommand=scrollbar.set, bg="black", fg="white")
    listbox.pack(side=tk.RIGHT, fill=tk.BOTH)
    # Attacher la scrollbar à la liste
    scrollbar.config(command=listbox.yview)
    new_bu = tk.Button(app, text="New", command=createTask)
    new_bu.place(relx=1, rely=1, anchor=tk.SE, bordermode=tk.OUTSIDE)
    create_optbar()
    trie_start()

    # Lier la fonction resize_listbox à l'événement de redimensionnement de la fenêtre
    app.bind("<Configure>", resize_listbox)
    # Attacher la fonction 'ouvrir_nouvelle_fenetre' à l'événement de double-clic
    listbox.bind('<Double-Button-1>', config_task)
    setting_bu = tk.Button(app, text="Settings", command=Settings.run)
    setting_bu.pack(side="left", anchor="sw")

    app.mainloop()

if __name__ == '__main__':
    appli()