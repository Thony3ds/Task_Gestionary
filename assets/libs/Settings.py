import Run_App
import tkinter as tk

def save():
    print("Saving") # TODO finish

def run():
    global app
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

    #END:
    bu_end = tk.Button(app, text="Save Settings", command=save)
    bu_end.pack(pady= 10)

    app.mainloop()