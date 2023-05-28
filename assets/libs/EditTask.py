import tkinter as tk
from tkinter import ttk
import os, datetime, json

def initing(path):
    file = open(path, "r")
    global data
    data = json.load(file)
    file.close()

def verif_state():
    if checkbox_var.get() == 1:
        var = "Do" # == Coché
    elif checkbox_var.get() == 0:
        var = "In process" # == non coché
    return var

def update_state():
    if checkbox_var.get() == 1:
        checkbox_var.set(0)
    else:
        checkbox_var.set(1)

def createState_var():
    # Variable pour stocker l'état du bouton à cocher
    global checkbox, checkbox_var
    checkbox_var = tk.IntVar()

    # Fonction de mise à jour de l'état
    # Création du bouton à cocher avec la variable associée
    checkbox = tk.Checkbutton(newt, text="Finish Task", variable=checkbox_var, command=update_state)
    checkbox.pack(pady=10)
    if data["State"] == "Do":
        checkbox.config(text="No Remove Do task")

def serialize_date(date):
    if isinstance(date, datetime.date):
        next_day = date + datetime.timedelta(days=1)
        return next_day.strftime('%d/%m/%Y')
    raise TypeError(f'Object of type {date.__class__.__name__} is not JSON serializable')

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
    new["State"] = verif_state()
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
    newf = open(thepath, "w+")
    newf.write(json_write)
    newf.close()
    newt.destroy()

def createDateEntry():
    global day_var, month_var, year_var
    # Extraire la date
    date_str = data["limit_date"]
    # Séparer la date en composantes jour, mois et année
    jour, mois, annee = date_str.split("/")
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
    day_entry.insert(0, jour)

    # Label et champ d'entrée pour le mois
    month_label = ttk.Label(date_frame, text="Mois:")
    month_label.grid(row=0, column=2, padx=5, pady=5)
    month_entry = ttk.Spinbox(date_frame, from_=1, to=12, width=5, textvariable=month_var)
    month_entry.grid(row=0, column=3, padx=5, pady=5)
    month_entry.insert(0, mois)

    # Label et champ d'entrée pour l'année
    year_label = ttk.Label(date_frame, text="Année:")
    year_label.grid(row=0, column=4, padx=5, pady=5)
    year_entry = ttk.Entry(date_frame, width=10, textvariable=year_var)
    year_entry.grid(row=0, column=5, padx=5, pady=5)
    year_entry.insert(0, annee)

def run(path):
    global thepath
    thepath = path
    global newt, inp_title, inp_desc, inp_category, date_actuelle
    date_actuelle = datetime.date.today()
    initing(path=path)
    newt = tk.Tk()
    newt.title("Edit Task")
    newt.geometry("500x500")
    newt.config(bg="black")
    newt.option_add('*Font', "Ubuntu")
    newt.option_add('*Label.foreground', 'white')
    newt.option_add('*Label.background', 'black')
    lab1 = tk.Label(newt, text="Title:")
    lab1.pack()
    inp_title = tk.Entry(newt)
    inp_title.pack(pady=10)
    inp_title.delete(0, tk.END)  # Supprimer le contenu actuel de l'Entry
    inp_title.insert(0, data["title"])  # Insérer le nouveau texte dans l'Entry
    lab2 = tk.Label(newt, text="Description:")
    lab2.pack(pady=10)
    inp_desc = tk.Entry(newt)
    inp_desc.pack(pady=10)
    inp_desc.delete(0, tk.END)  # Supprimer le contenu actuel de l'Entry
    inp_desc.insert(0, data["description"])  # Insérer le nouveau texte dans l'Entry
    inp_desc.config(width=40)
    lab3 = tk.Label(newt, text="Date Limite:")
    lab3.pack(pady=10)
    createDateEntry()
    lab4 = tk.Label(newt, text="Category:")
    lab4.pack(pady=10)
    inp_category = tk.Entry(newt)
    inp_category.pack(pady=10)
    inp_category.delete(0, tk.END)  # Supprimer le contenu actuel de l'Entry
    inp_category.insert(0, data["category"])  # Insérer le nouveau texte dans l'Entry
    createState_var()
    bu = tk.Button(newt, text="Save", command=createTask2)
    bu.pack(pady=10)