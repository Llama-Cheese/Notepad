import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class Notepad:
    def __init__(self, master):
        self.master = master
        self.master.title("Notepad")
        self.master.geometry("500x500")

        self.text = tk.Text(self.master, wrap="word")
        self.text.pack(fill="both", expand=True)

        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.master)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        self.master.config(menu=menubar)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                self.text.delete("1.0", "end")
                self.text.insert("1.0", file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text.get("1.0", "end"))
                messagebox.showinfo("Notepad", "File saved successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop(
