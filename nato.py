from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Create a dict for NATO alphabet
nato_dict = {
    'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
    'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett',
    'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
    'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee',
    'Z': 'Zulu'
}

# List of words
list_of_words = ["Peter Piper", "Brown fox", "Forgive me", "The best", "Love you", "Donald duck"]

# Make function to make nato alphabet
def main():
    make_up = phrase.get(1.0, "end")
    sugg = combo.get()

    if make_up != "\n" and sugg == "":
        nato(make_up)
    elif make_up == "\n" and sugg != "":
        nato(sugg)
    elif make_up != "\n" and sugg != "":
        nato(make_up)
    else:
        error = messagebox.showerror(title="Error", message="Be sure that at least one of the inputs is given")

    var.set("")
    phrase.delete(1.0, "end")

def nato(word):
    nato_word = []
    for char in word:
        if char.upper() in list(nato_dict.keys()):
            nato_word.append(f"{char.upper()}: {nato_dict[char.upper()]}\n")
        else:
            nato_word.append(f"{char.upper()}: -\n")
    message = "\n".join(nato_word)
    final = messagebox.showinfo(title="Operation done", message=message)

# Start
root =Tk()
root.resizable(0, 0)
root.title("Nato")
root.geometry("450x240")

welcome = ttk.Label(root, text="Welcome to our NATO Alphabet Game", font="Arial 18 bold")
welcome.grid(row=0, column=0, columnspan=5, sticky="ew", padx=5, pady=10)

l_suggested = ttk.Label(root, text="Suggested Phrases:-")
l_suggested.grid(row=1, column=0, padx=2, pady=10)

var = StringVar()
combo = ttk.Combobox(root, values=list_of_words, textvariable=var)
combo.state(["readonly"])
combo.grid(row=1, column=1, pady=10, sticky="ew")

combo_button = ttk.Button(root, text="Clear", width=5, command=lambda: var.set(""))
combo_button.grid(row=1, column=4, padx=2, pady=10)

label = ttk.Label(root, text="Or Just write your own:-")
label.grid(row=2, column=0, padx=2, pady=10, sticky='nw')


phrase = Text(
    root,
    font=("Segoe UI", 10 ,"normal"),
    relief="solid",
    bd=1,
    height=5,
    width=30
)

scrollbar = ttk.Scrollbar(root, orient="vertical", command=phrase.yview)
scrollbar.grid(row=2, column=2, sticky="ns")
phrase.config(yscrollcommand=scrollbar.set)

phrase.grid(row=2, column=1, sticky="ns")

convert = ttk.Button(root, text="Convert to NATO", command=main)
convert.grid(row=3, column=1, pady=10)
root.mainloop()
