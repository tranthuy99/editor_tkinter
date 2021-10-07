import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r", encoding='utf8') as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"HELLO B*TCH - {filepath}")

def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w", encoding='utf8') as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"HELLO B*TCH - {filepath}")

window = tk.Tk()
window.geometry("1000x790")
window.title("HELLO B*TCH")
window.rowconfigure(0, minsize=600, weight=1)
window.columnconfigure(1, minsize=500, weight=1)

xscrollbar = tk.Scrollbar(window, orient=tk.HORIZONTAL)
xscrollbar.grid(row=3, column=1, sticky='ew')

yscrollbar = tk.Scrollbar(window)
yscrollbar.grid(row=0, column=3, sticky='ns')

txt_edit = tk.Text(window,wrap=tk.WORD, undo=True, maxundo=-1)
txt_edit.config(font='Helvetica 12 ', insertbackground='white', spacing1=15, spacing2=7, fg='white', bg='black')
txt_edit.config(xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
txt_edit.focus_set()

xscrollbar.config(command=txt_edit.xview)
yscrollbar.config(command=txt_edit.yview)

fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")




def add_BRAND(event):
    txt_edit.insert(tk.SEL_FIRST,' <BRA> ')
    txt_edit.insert(tk.SEL_LAST,' </BRA> ' )

def add_CAT(event):
    txt_edit.insert(tk.SEL_FIRST,' <CAT> ')
    txt_edit.insert(tk.SEL_LAST,' </CAT> ' )

def add_PRODUCT(event):
    txt_edit.insert(tk.SEL_FIRST,' <PRO> ')
    txt_edit.insert(tk.SEL_LAST,' </PRO> ' )
            

window.bind('<Control-p>', add_PRODUCT)
window.bind('<Control-C>', add_CAT)
window.bind('<Control-b>', add_BRAND)
window.bind('<Control-o>', open_file)
window.bind('<Control-s>', save_file)
window.bind('<Control-z>', txt_edit.edit_undo)


window.mainloop()
