import tkinter as tk

app = tk.Tk()
app.option_add('*Font', "Ubuntu")
app.option_add('*Label.foreground', 'white')
app.option_add('*Label.background', 'black')


def appli():
    app.title("Gestionnaire de Taches")
    app.geometry("500x500")
    app.config(bg="black")

    lab1 = tk.Label(app, text="Task Gestionary")
    lab1.place(x=0, y=0)

    # Créer une scrollbar
    global scrollbar, listbox
    scrollbar = tk.Scrollbar(app)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    # Créer une liste
    listbox = tk.Listbox(app, yscrollcommand=scrollbar.set, bg="black", fg="white")
    listbox.pack(side=tk.RIGHT, fill=tk.BOTH)
    # Attacher la scrollbar à la liste
    scrollbar.config(command=listbox.yview)


    app.mainloop()

if __name__ == '__main__':
    appli()