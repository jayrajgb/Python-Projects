import tkinter
from tkinter import *

root = Tk()
root.title("DICOM Image Encryption/Decryption System")

root.geometry("960x480")

# root.minsize(840,420)
# root.maxsize(1200, 600)

# from PIL import Image, ImageTk
# img = Image.open("1.jpg")
# photo = ImageTk.PhotoImage(img)
# label = Label(image=photo)
# label.pack()


### Extra Tips
# root.wm_iconbitmap("1.ico") --- set icon
# root.configure(background = "grey") --- set bg
# root.winfo_screenwidth() --- get screen width
# root.winfo_screenheight() --- get screen height
# Button(root,command = root.destroy).pack() --- close the root


### Widgets
# Label
# Frame
# Button
# Entry
# Checkbutton
# Canvas

### Important label options
# text -- adds text
# bd -- background
# fg -- foreground
# font -- set font --- (font = "timesnewroman 16 bold")
# padx -- x padding
# pady -- y padding
# relief -- border styling - SUNKEN, RAISED, GROOVE, RIDGE
# borderwidth -- set width of border --- can help to the size of frames and adjust accordingly


### Important pack options
# anchor = nw, ne, sw, se
# side = top, bottom, left, right (in capital)
# fill = x, y (in capital) --- gets stretched throughout the Y or X axis
# padx, pady --- for packing --- like margins


### Frame -- frame is like a div
# f1 = Frame(root, borderwidth=20)
# f1.pack()
# l = Label(f1, text = "label gets added to f1")
# l.pack()


### Buttons
# b1 = Button(frame, text = "Print", command = hello) --- this will call function hello()
# b1.pack()


### Grid --- Method of packing
# user = Lable(root, text = "Username")
# pass = Lable(root, text = "Password")
# user.grid() --- row = 0, column = 0
# pass.grid(row = 1)  --- column = 0

# Variable classes
# BooleanVar, DoubleVar, IntVar, StringVar

# uservalue = StringVar()
# passvalue = StringVar()
# userentry = Entry(root, textvariable = uservalue)
# passentry = Entry(root, textvariable = passvalue)

# userentry.grid(row = 0, column = 1)
# passentry.grid(row = 1, column = 1)

# Button(text = "Submit", command = getval).grid() --- one liner

# def getval():
#   username = uservalue.get()
#   password = passvalue.get()
#   print(f"The username is {username}, and the password is {password}")
### Grid End


### Checkbox
# isNerd = IntVar()
# football = Checkbutton(text = "Love football?", variable = isNerd)


### Radiobutton
# var = StringVar()
# var.set("null")
# radio = Radiobutton(root, text = "Dosa", value = "dosa", variable = var).pack()
# radio = Radiobutton(root, text = "Idli", value = "idli", variable = var).pack()
# radio = Radiobutton(root, text = "Pohe", value = "pohe", variable = var).pack()
# order = var.get()
# tmsg.showinfo("Order", f"Received order for {order}")

### Event
# def myevent(event):
#   print("Some function")
# mybutton = Button(root, text = "Click to run the event")
# mybutton.bind('<Button-1>', myevent)
# mybutton.bind('<Double-1>', quit)


### Menu
# mymenu = Menu(root)
# mymenu.add_command(label = "File", command = myfunc)
# mymenu.add_command(label = "Tools", command = myfunc)
# mymenu.add_command(label = "Help", command = myfunc)
# root.config(menu = mymenu) --- These are used to create non-dropdown menu

# mymenubar is filemenu/mainmenu
# mymenubar = Menu(root) --- menu for root
# m1 = Menu(mymenubar) --- submenu of mymenubar/ menu for mymenubar
# m1 = Menu(mymenubar, tearoff = 0) --- remove te tearoff option/ horizontal line option
# m1.add_command(label = "New", command = myfunc)
# m1.add_command(label = "Open", command = myfunc)
# m1.add_separator()
# m1.add_command(label = "Save", command = myfunc)
# root.config(menu = mymenubar)
# mymenubar.add_cascade(label = "File", menu = m1)


### Message Box
# import tkinter.messagebox as tmsg
# tmsg.showinfo("Info", "Eat. Sleep. Drink. Football") --- example 1
# yesno = tmsg.askquestion("Question", "Love Football?") --- example 2
# if yesno == "yes":
#   msg = "Suiiii..."
# else:
#   msg = "Meheheh...ssi"
# tmsg.showinfo("Info", msg)


### Listbox
# lbx = Listbox(root)
# lbx.pack()
# lbx.insert(ACTIVE, "Adds the list item above selected list item")
# lbx.insert(END, "Adds the list item at the end of the list")


### Scrollbar
# widget(yscrollcommand = scrollbar.set) --- to connect to a widget
# scrollbar.config(command = widget.yview)
# text = Text(root, yscrollcommand = scrollbar.set)
# text.pack(fill = BOTH)
# scrollbar.config(command = text.yview)


### Classes and Objects
# class GUI(Tk):                      --- GUI is the class, self is the root
#     def __int__(self):              --- Constructor
#         super().__init__()
#         self.geometry("960x480")
#
#     def click(self):
#         print("Button clicked")
#
#     def addbutton(self, inptext):
#         Button(text=inptext, command=self.click).pack()
#
# if __name__ == '__main__':
#     window = GUI()                  --- window is the object, and is the root
#     window.addbutton("Click me")
#
#     window.mainloop()


### Filedialog
# from tkinter.filedialog import askopenfilename, asksaveasfilename
# def openFile():
#     global file
#     file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*", "*.text")]





root.mainloop()