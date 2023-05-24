import tkinter as tk
from tkinter import ttk
import os, datetime, json

app = tk.Tk()
app.option_add('*Font', "Ubuntu")
app.option_add('*Label.foreground', 'white')
app.option_add('*Label.background', 'black')
global data_actuelle
date_actuelle = datetime.date.today()

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
    day_value = day_var.get()
    month_value = month_var.get()
    year_value = year_var.get()
    if day_value and month_value and year_value:
        inp_date = "{}/{}/{}".format(day_value, month_value, year_value)
        new["limit_date"] = inp_date
    else:
        new["limit_date"] = date_actuelle + datetime.timedelta(days=1)  # Ou une valeur par défaut si aucune date n'est entrée
    new["category"] = creat_catego # TODO temporaire
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
    newt.quit()

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
    global newt, inp_title, inp_desc # TODO inp_category
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
    lab4 = tk.Label(newt, text="Category: (In Build for wait catego = Normal)")
    lab4.pack(pady=10)
    global creat_catego
    creat_catego = "Normal"
    #TODO TO CODE
    bu = tk.Button(newt, text="Create", command=createTask2)
    bu.pack(pady=10)

def appli():
    app.title("Gestionnaire de Taches")
    app.geometry("500x500")
    app.config(bg="black")

    lab1 = tk.Label(app, text="Task Gestionary")
    lab1.place(x=0, y=0)

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

    app.mainloop()

if __name__ == '__main__':
    appli()