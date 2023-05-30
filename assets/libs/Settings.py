import Run_App, json
import tkinter as tk

def initing():
    global data
    f = open("assets/config/settings.json", "r")
    data = json.load(f)
    f.close()

def save():
    print("Saving")  # TODO finish
    tosave = {}
    try:
        tosave["task_max"] = int(bu_maxt.get())
        # SUITE ...
    except ValueError:
        tosave["task_max"] = data["task_max"]
        # SUITE ...
    # TODO temporaire
    tosave["notif_rights"] = "True"
    f = open("assets/config/settings.json", "w")
    f.write(json.dumps(tosave))
    f.close()

def run():
    global app, bu_maxt
    initing()
    app = tk.Tk()
    app.option_add('*Font', "Ubuntu")
    app.option_add('*Label.foreground', 'white')
    app.option_add('*Label.background', 'black')
    app.title("Settings")
    app.geometry("500x500")
    app.config(bg="black")

    lab1 = tk.Label(app, text="Task max (a very big number can create bugs in the app):")
    lab1.pack()
    bu_maxt = tk.Entry(app)
    bu_maxt.pack()
    bu_maxt.insert(0, data["task_max"])

    # END:
    bu_end = tk.Button(app, text="Save Settings", command=save)
    bu_end.pack(pady=10)

    app.mainloop()

    #END:
    bu_end = tk.Button(app, text="Save Settings", command=save)
    bu_end.pack(pady=10)

    app.mainloop()