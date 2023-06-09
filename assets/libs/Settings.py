import Run_App, json, os
import tkinter as tk

def initing():
    global data
    f = open("assets/config/settings.json", "r")
    data = json.load(f)
    f.close()

def debug_app():
    print("Check requirments")
    os.system("pip3 install gitpython")
    print("Update requirment --> DO")
    print("Finish Debuger if you have more bug use the settings of start")

def save():
    print("Saving")  # TODO finish
    tosave = {}
    try:
        tosave["task_max"] = int(bu_maxt.get())
    except ValueError:
        tosave["task_max"] = data["task_max"]
    f = open("assets/config/settings.json", "w")
    f.write(json.dumps(tosave))
    f.close()
    print("Saved Settings")
    app.destroy()

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
    bu_debug = tk.Button(app, text="Use Debug App/ Check requirments", command=debug_app)
    bu_debug.pack(pady=10)

    #END:
    bu_end = tk.Button(app, text="Save Settings", command=save, fg="green")
    bu_end.pack(pady=10)

    app.mainloop()